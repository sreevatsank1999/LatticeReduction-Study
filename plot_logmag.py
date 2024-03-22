import pickle
from fpylll.tools.bkz_plot import plot_gso_norms
from math import *

import matplotlib.pyplot as plt

import os

from utils.plot import plot_traces

def maplog2(l):
    return [log(l[i], 2) for i in range(len(l))]

def plot_gso_norms_in_out(gso_norms, basename="gso-norms",
                   extension="png", dpi=300):
    """Plot ``gso_norms``.

    :param gso_norms: list of GSO norms. It is assumed these follow the form output by ``KeepGSOBKZ``.
    :param basename: graphics filename basenname (may contain full path)
    :param extension: graphics filename extension/type
    :param dpi: resolution

    :returns: Tuple of filenames written.
    """

    # Ensure matplotlib does not use any Xwindows backend
    plt.switch_backend('Agg')
    
    # Create a figure and an axis
    fig, ax = plt.subplots()
        
    d = len(gso_norms[0][0][1])
    x = range(1,d+1)

    ax.plot(x, maplog2(gso_norms[0][0][1]), label="Input", linewidth=2)
    ax.plot(x, maplog2(gso_norms[-1][-1][1]), label="Output", linewidth=2)

    ax.set_title("$\\|\\mathbf{b}_i^*\\|$")
    ylim = ax.get_ylim()

    ax.set_ylabel("$2\\,\\log_2(\\cdot)$")
    ax.set_xlabel("$i$")
    ax.legend(loc="upper right")
    ax.set_ylim(*ylim)

    fullname = "%s.%s"%(basename, extension)
    fig.savefig(fullname, dpi=dpi)
    plt.close()





# Load results
algo = "slide";
if algo == "bkz":
    filename = "BKZ-convergence-2024-03-21_15-06-56.pickle"
    exp_name="BKZ"          # experiment name
elif algo == "sdbkz":
    filename = "SDBKZ-convergence-2024-03-21_15-07-42.pickle"
    exp_name="SDBKZ"          # experiment name
elif algo == "slide":
    filename = "Slide-convergence-2024-03-21_15-08-40.pickle"
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

plot_gso_norms_in_out(results["gso_norms"], basename=f"{outdir}/{exp_name}-log_mag")