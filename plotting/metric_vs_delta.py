import pickle
from utils.plot import extract_traces, plot_traces, trace_param, normalize_traces


def plot_delta(results, dims, ks, deltas, outdir):
    # Plot Orthogonal Defect vs. BKZ delta
    trace = "ldelta"   # orthogonal defect
    filename = f"{outdir}/BKZ-orthogonal_defect_vs_delta_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 2, 0);
    plot_traces(traces, "Orthogonal Defect ($\Delta$) vs. BKZ $\delta$", "$\delta$", "$log(\Delta)$", filename)
    
    filename = f"{outdir}/BKZ-orthogonal_defect_vs_delta_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, "Orthogonal Defect ($\Delta$) vs. BKZ $\delta$", "$\delta$", "$log(\Delta)_{norm}$", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##


    # Plot CPU time vs. BKZ Delta
    trace = "cputime"   
    filename = f"{outdir}/BKZ-cputime_vs_delta_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 2, 0);
    plot_traces(traces, "CPU Time vs. BKZ $\delta$", "$\delta$", "t", filename)
    
    filename = f"{outdir}/BKZ-cputime_vs_delta_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, "CPU Time vs. BKZ $\delta$", "$\delta$", "$t_{norm}$", filename)

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
    
    filename = f"{outdir}/BKZ-orthogonal_defect_vs_kappa_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, "Orthogonal Defect ($\Delta$) vs. BKZ $\kappa$", "$\kappa$", "$log(\Delta)_{norm}$", filename)

    ## ------------------------------------------------------------------------------------------------------------------------------ ##


    # Plot CPU time vs. BKZ Kappa
    trace = "cputime"   
    filename = f"{outdir}/BKZ-cputime_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0);
    plot_traces(traces, "CPU Time vs. BKZ $\kappa$", "$\kappa$", "t", filename)
    
    filename = f"{outdir}/BKZ-cputime_vs_kappa_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, "CPU Time vs. BKZ $\kappa$", "$\kappa$", "$t_{norm}$", filename)

    ## ------------------------------------------------------------------------------------------------------------------------------ ##
    
    
    # Plot hv ratio vs. BKZ Kappa
    trace = "hv/hv"   
    filename = f"{outdir}/BKZ-hvr_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0);
    plot_traces(traces, "Half Volume ratio ($\\nu$) vs. BKZ $\kappa$", "$\kappa$", "$\\nu$", filename)

    filename = f"{outdir}/BKZ-hvr_vs_kappa_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, "Half Volume ratio ($\\nu$) vs. BKZ $\kappa$", "$\kappa$", "$\\nu_{norm}$", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##


    # Plot rhf  vs. BKZ Kappa
    trace = "rhf"   
    filename = f"{outdir}/BKZ-rhf_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0);
    plot_traces(traces, "Root Hermit Factor ($\gamma$) vs. BKZ $\kappa$", "$\kappa$", "$\gamma$", filename, ylim = [0.96,1.03])

    filename = f"{outdir}/BKZ-rhf_vs_kappa_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, "Root Hermit Factor ($\gamma$) vs. BKZ $\kappa$", "$\kappa$", "$\gamma_{norm}$", filename, ylim = [0.98,1.0])
    ## ------------------------------------------------------------------------------------------------------------------------------ ##