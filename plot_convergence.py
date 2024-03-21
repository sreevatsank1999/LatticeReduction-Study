import pickle
from fpylll.tools.bkz_plot import plot_gso_norms
from math import *

import os

from utils.plot import plot_traces

def maplog2(l):
    return [log(l[i], 2) for i in range(len(l))]

def plot_gso_norms_sparse(gso_norms, block_size, start=0, stop=-1, step=5, basename="bkz-gso-norms",
                   extension="png", dpi=300):
    """Plot ``gso_norms``.

    :param gso_norms: list of GSO norms. It is assumed these follow the form output by ``KeepGSOBKZ``.
    :param block_size: BKZ block size
    :param basename: graphics filename basenname (may contain full path)
    :param extension: graphics filename extension/type
    :param dpi: resolution

    :returns: Tuple of filenames written.

    .. note:: To convert to movie, call e.g. ``ffmpeg -framerate 8 -pattern_type glob -i "*.png" bkz.mkv``

    .. warning:: This function is quite slow.
    """
    from math import log, pi, e
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    filenames = []

    def plot_finalize(ax, name):
        ax.set_ylabel("$2\\,\\log_2(\\cdot)$")
        ax.set_xlabel("$i$")
        ax.legend(loc="upper right")
        ax.set_ylim(*ylim)

        fullname = "%s.%s"%(name, extension)
        fig.savefig(fullname, dpi=dpi)
        filenames.append(fullname)
        plt.close()

    d = len(gso_norms[start][0][1])
    x = range(1,d+1)

    beta = float(block_size)
    delta_0 = (beta/(2.*pi*e) * (pi*beta)**(1./beta))**(1./(2.*(beta-1)))
    alpha = delta_0**(-2.*d/(d-1.))
    logvol = sum(maplog2(gso_norms[start][0][1]))  # already squared
    gsa = [log(alpha, 2)*(2*i) + log(delta_0, 2)*(2*d) + logvol*(1./d) for i in range(d)]

    fig, ax = plt.subplots()
    ax.plot(x, maplog2(gso_norms[start][0][1]), label="$\\|\\mathbf{b}_i^*\\|$")
    ylim = ax.get_ylim()
    ax.set_title("Input")
    plot_finalize(ax, "%s-aaaa-input"%basename)

    for i, tour in enumerate(gso_norms[start+1:stop-1]):
        if i%step != 0:
            continue
        
        j = len(tour);
        (kappa, norms) = tour[-1];
        # for j, (kappa, norms) in enumerate(tour):
        fig, ax = plt.subplots()

        # rect = patches.Rectangle((kappa, ylim[0]), min(block_size, d-kappa-1), ylim[1]-ylim[0],
                                    # fill=True, color="lightgray")
        # ax.add_patch(rect)
        ax.plot(x, maplog2(norms), label="$\\|\\mathbf{b}_i^*\\|$")
        ax.plot(x, gsa, color="black", label="GSA")
        ax.set_title("BKZ-%d tour: %2d, $\\kappa$: %3d"%(block_size, i, kappa))
        plot_finalize(ax, "%s-t%03d-%04d"%(basename, i, j))

    fig, ax = plt.subplots()
    ax.plot(x, maplog2(gso_norms[stop][-1][1]))
    ax.set_title("Output")
    plot_finalize(ax, "%s-zzzz-output"%basename)

    return tuple(filenames)




# Load results
algo = "slide";
if algo == "bkz":
    filename = "BKZ-convergence-2024-03-21_04-26-48.pickle"
    exp_name="BKZ"          # experiment name
elif algo == "sdbkz":
    filename = "SDBKZ-convergence-2024-03-21_09-25-31.pickle"
    exp_name="SDBKZ"          # experiment name
elif algo == "slide":
    filename = "Slide-convergence-2024-03-21_14-48-27.pickle"
    exp_name="Slide"          # experiment name
else:
    raise ValueError("Invalid algorithm")

# filename = "Slide-convergence-2024-03-21_14-48-27.pickle"
results = pickle.load(open(f"results/{filename}", "rb"));


outdir = "results/plots/"+ filename.split(".")[0]
try:
    os.mkdir(outdir);
except(FileExistsError):
    pass

plot_gso_norms_sparse(results["gso_norms"], results["blocksize"], start=0, stop=50, step=2, basename=f"{outdir}/{exp_name}-gso-norms")


gso_norms = results["gso_norms"];
block_size = results["blocksize"];

indx = [0,3,7,15,31,63]
traces = {};
for i, tour in enumerate(gso_norms[0:-1]):
    (kappa, norms) = tour[-1];
    log_norm = maplog2(norms);
    
    for bi in indx:
        str_bi = "$\\|\\mathbf{b}_{bi}^*\\|$".format(b="{b}", bi="{"+f"{bi}"+"}");
        if str_bi not in traces:
            traces[str_bi] = ([],[],[]);
        traces[str_bi][0].append(i);
        traces[str_bi][1].append(log_norm[bi]);
        traces[str_bi][2].append(0);
        
plot_traces(traces, f"{exp_name} convergence", f"{exp_name} tour", "$2\\,\\log_2(\\cdot)$", f"results/plots/{exp_name}-convergence.png", yscale = 'linear')