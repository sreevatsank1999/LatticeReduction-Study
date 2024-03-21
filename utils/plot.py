from math import *
import numpy as np

import matplotlib.pyplot as plt


traces_ty = {
    "cputime": "cputime",
    "r_0": "b0",
    "rhf": "hf",
    "ldelta": "orthogonality_defect",
    "hv/hv": "half_volume_ratio"
}

def extract_traces(results, trace_param, xi, zi):
    traces = {};
    
    for param in trace_param:
        x, std = get_sample(results, *param);
        if x is None:
            continue;
        if param[zi] not in traces:
            traces[param[zi]] = ([],[],[]);
        traces[param[zi]][0].append(param[xi]);
        traces[param[zi]][1].append(x);
        traces[param[zi]][2].append(std);
    return traces

def get_sample(results, dim,k,delta,trace):
    
    algo = f"BKZ-d{delta}";
    try:
        nbSample = len(results[dim][k][algo]);
        samples = [float(results[dim][k][algo][i][1].data[trace]) for i in range(nbSample)];
    except:
        print(f"Missing data for dim={dim}, k={k}, delta={delta}, trace={trace}");
        return None,None;
    
    x = np.mean(samples);
    std = np.std(samples);
    
    return x,std

def get_samples_raw(results, dim,k,algo,trace):
    
    nbSample = len(results[dim][k][algo]);
    samples = [results[dim][k][algo][i][1].data[trace] for i in range(nbSample)];
    
    return samples
    

def plot_traces(traces, title, xlabel, ylabel, filename, nsigma=2, ycscale = 'linear'):

    # Ensure matplotlib does not use any Xwindows backend
    plt.switch_backend('Agg')

    if ycscale == 'log':
        plt.semilogy();
        
    # Create a figure and an axis
    fig, ax = plt.subplots()

    for name,(x, trace,std) in traces.items():
        x = np.array(x); trace = np.array(trace); std = np.array(std);
        # Random select marker 
        marker = np.random.choice(['o', 's', 'D', 'x', '+'])
        ax.plot(x, trace, label=name, linewidth=2, marker=marker, markersize=7)  # Thicker lines, markers added
        ax.fill_between(x, trace - nsigma * std, trace + nsigma * std, alpha=0.55) # Shaded error region

    # Adding legend to the plot with larger font size
    ax.legend(fontsize='large')
    ax.set_yscale(ycscale);
    
    # Adding title and labels with larger font size
    ax.set_title(title, fontsize='x-large')
    ax.set_xlabel(xlabel, fontsize='large')
    ax.set_ylabel(ylabel, fontsize='large')
    ax.grid(True)
    
    # Increase tick label size
    ax.tick_params(axis='both', which='major', labelsize='x-large')

    # Save the plot to disk as an image file
    plt.savefig(filename, dpi=300)

    # Close the plot figure to free up memory
    plt.close(fig)


def trace_param(dims, ks, deltas, trace):
    return [(dim, k, delta, trace) for dim in dims for k in ks for delta in deltas]