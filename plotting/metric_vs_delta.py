import pickle
from utils.plot import extract_traces, plot_traces, trace_param, normalize_traces


def plot_delta(results, dims, ks, deltas, outdir, exp_name):
    # Plot Orthogonal fDefect vs. {exp_name} delta
    trace = "ldelta"   # orthogonal defect
    filename = f"{outdir}/{exp_name}-orthogonal_defect_vs_delta_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 2, 0,exp_name);
    plot_traces(traces, f"Orthogonal Defect ($\Delta$) vs. {exp_name} $\delta$", "$\delta$", "$log(\Delta)$", filename)
    
    filename = f"{outdir}/{exp_name}-orthogonal_defect_vs_delta_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, f"Orthogonal Defect ($\Delta$) vs. {exp_name} $\delta$", "$\delta$", "$log(\Delta)_{norm}$", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##


    # Plot CPU ftime vs. {exp_name} Delta
    trace = "cputime"   
    filename = f"{outdir}/{exp_name}-cputime_vs_delta_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 2, 0,exp_name);
    plot_traces(traces, f"CPU Time vs. {exp_name} $\delta$", "$\delta$", "t", filename)
    
    filename = f"{outdir}/{exp_name}-cputime_vs_delta_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, f"CPU Time vs. {exp_name} $\delta$", "$\delta$", "$t_{norm}$", filename)

    ## ------------------------------------------------------------------------------------------------------------------------------ ##



def plot_kappa(results, dims, ks, deltas, outdir, exp_name):
    # create tuples of all possible combinations of (dim, k, algo)

    # Plot Orthogonal fDefect vs. {exp_name} Kappa
    trace = "ldelta"   # orthogonal defect
    filename = f"{outdir}/{exp_name}-orthogonal_defect_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0,exp_name);
    plot_traces(traces, f"Orthogonal Defect ($\Delta$) vs. {exp_name} $\kappa$", "$\kappa$", "$log(\Delta)$", filename)
    
    filename = f"{outdir}/{exp_name}-orthogonal_defect_vs_kappa_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, f"Orthogonal Defect ($\Delta$) vs. {exp_name} $\kappa$", "$\kappa$", "$log(\Delta)_{norm}$", filename)

    ## ------------------------------------------------------------------------------------------------------------------------------ ##


    # Plot CPU ftime vs. {exp_name} Kappa
    trace = "cputime"   
    filename = f"{outdir}/{exp_name}-cputime_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0,exp_name);
    plot_traces(traces, f"CPU Time vs. {exp_name} $\kappa$", "$\kappa$", "t", filename)
    
    filename = f"{outdir}/{exp_name}-cputime_vs_kappa_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, f"CPU Time vs. {exp_name} $\kappa$", "$\kappa$", "$t_{norm}$", filename)

    ## ------------------------------------------------------------------------------------------------------------------------------ ##
    
    
    # Plot hv fratio vs. {exp_name} Kappa
    trace = "hv/hv"   
    filename = f"{outdir}/{exp_name}-hvr_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0,exp_name);
    plot_traces(traces, f"Half Volume ratio ($\\nu$) vs. {exp_name} $\kappa$", "$\kappa$", "$\\nu$", filename)

    filename = f"{outdir}/{exp_name}-hvr_vs_kappa_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, f"Half Volume ratio ($\\nu$) vs. {exp_name} $\kappa$", "$\kappa$", "$\\nu_{norm}$", filename)
    ## ------------------------------------------------------------------------------------------------------------------------------ ##


    # Plot rhf f vs. {exp_name} Kappa
    trace = "rhf"   
    filename = f"{outdir}/{exp_name}-rhf_vs_kappa_n_dim.png";

    # create tuples of all possible combinations of (dim, k, algo)
    params = trace_param(dims, ks, deltas, trace);

    traces = extract_traces(results, params, 1, 0,exp_name);
    plot_traces(traces, f"Root Hermit Factor ($\gamma$) vs. {exp_name} $\kappa$", "$\kappa$", "$\gamma$", filename, ylim = [0.96,1.03])

    filename = f"{outdir}/{exp_name}-rhf_vs_kappa_n_dim_norm.png";
    traces = normalize_traces(traces);
    plot_traces(traces, f"Root Hermit Factor ($\gamma$) vs. {exp_name} $\kappa$", "$\kappa$", "$\gamma_{norm}$", filename, ylim = [0.98,1.0])
    ## ------------------------------------------------------------------------------------------------------------------------------ ##