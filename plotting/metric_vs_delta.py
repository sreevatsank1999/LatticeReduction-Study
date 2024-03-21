import pickle
from utils.plot import extract_traces, plot_traces, trace_param


def plot_delta(results, dims, ks, deltas, outdir):
    # Plot Orthogonal Defect vs. BKZ delta
    trace = "ldelta"   # orthogonal defect
    filename = f"{outdir}/BKZ-orthogonal_defect_vs_delta_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 2, 0);

    plot_traces(traces, "Orthogonal Defect ($\Delta$) vs. BKZ $\delta$", "$\delta$", "$log(\Delta)$", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##


    # Plot CPU time vs. BKZ Delta
    trace = "cputime"   
    filename = f"{outdir}/BKZ-cputime_vs_delta_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 2, 0);

    plot_traces(traces, "CPU Time vs. BKZ $\delta$", "$\delta$", "t", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##



def plot_kappa(results, dims, ks, deltas, outdir):
    # create tuples of all possible combinations of (dim, k, algo)

    # Plot Orthogonal Defect vs. BKZ Kappa
    trace = "ldelta"   # orthogonal defect
    filename = f"{outdir}/BKZ-orthogonal_defect_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0);

    plot_traces(traces, "Orthogonal Defect ($\Delta$) vs. BKZ $\kappa$", "$\kappa$", "$log(\Delta)$", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##


    # Plot CPU time vs. BKZ Kappa
    trace = "cputime"   
    filename = f"{outdir}/BKZ-cputime_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0);

    plot_traces(traces, "CPU Time vs. BKZ $\kappa$", "$\kappa$", "t", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##
    
    
    # Plot hv ratio vs. BKZ Kappa
    trace = "hv/hv"   
    filename = f"{outdir}/BKZ-hvr_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0);

    plot_traces(traces, "Half Volume ratio ($\\nu$) vs. BKZ $\kappa$", "$\kappa$", "$\\nu$", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##


    # Plot hv ratio vs. BKZ Kappa
    trace = "rhf"   
    filename = f"{outdir}/BKZ-rhf_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0);

    plot_traces(traces, "Root Hermit Factor ($\gamma_k$) vs. BKZ $\kappa$", "$\kappa$", "$\gamma_k$", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##