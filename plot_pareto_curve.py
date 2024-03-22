import matplotlib.pyplot as plt
import numpy as np

from utils.plot import extract_traces, plot_traces, trace_param, normalize_traces, get_sample

import pickle

# Define the function to plot similar kind of graph
def plot_pareto_curve(points_info, traces, title, xlabel, ylabel, filename):

    # Ensure matplotlib does not use any Xwindows backend
    plt.switch_backend('Agg')
    
    # Create a figure and an axis
    fig, ax = plt.subplots()
        
    # Mark the points of interest
    for point, label, mark in points_info:
        ax.plot(point[0], point[1], mark[0], label=label, markersize=15, markerfacecolor=mark[1], markeredgecolor='black')
        ax.text(point[0]+point[2], point[1], label, fontsize=12, bbox=dict(facecolor='white', alpha=0.25))
    
    for (x,y,lbl,l) in traces:
        ax.plot(x,y, l, label=lbl, linewidth=1.5, alpha=0.85)
    
    # Set the labels and title
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # invert yaixs
    ax.invert_yaxis()
    
    # Add a grid
    ax.grid(True, which="both", ls="--", linewidth=0.5)


    # Save the plot to disk as an image file
    plt.savefig(filename, dpi=300)

    # Close the plot figure to free up memory
    plt.close(fig)

# Load results
bkz_filename = "BKZ-2024-03-21_15-34-42.pickle"
sdbkz_filename = "SDBKZ-2024-03-21_19-15-46.pickle"
slide_filename = "Slide-2024-03-21_18-27-57.pickle"


bkz_results = pickle.load(open(f"results/{bkz_filename}", "rb"))
sdbkz_results = pickle.load(open(f"results/{sdbkz_filename}", "rb"))
slide_results = pickle.load(open(f"results/{slide_filename}", "rb"))

dims = [128];
ks = [2, 4, 8, 16, 32];
xtrace = "cputime";
ytrace = "ldelta";
deltas = [0.99]

pts = trace_param(dims, ks, deltas, [None]);

points_info = [];
dot_traces = [];

dot_trace = ([],[], "BKZ", 'g--');
for pt in pts:
    x, _ = get_sample(bkz_results, pt[0], pt[1], pt[2], xtrace, "BKZ");
    y, _ = get_sample(bkz_results, pt[0], pt[1], pt[2], ytrace, "BKZ");
    points_info.append(((x,y,4), f"{pt[1]}-BKZ", ('o', 'green')));
    dot_trace[0].append(x);
    dot_trace[1].append(y);
dot_traces.append(dot_trace);

dot_trace = ([],[], "SDBKZ", 'r--');
for pt in pts:
    x, _ = get_sample(sdbkz_results, pt[0], pt[1], pt[2], xtrace, "SDBKZ");
    y, _ = get_sample(sdbkz_results, pt[0], pt[1], pt[2], ytrace, "SDBKZ");
    points_info.append(((x,y,2), f"{pt[1]}-SDBKZ", ('^', 'red')));
    dot_trace[0].append(x);
    dot_trace[1].append(y);
dot_traces.append(dot_trace);


dot_trace = ([],[], "Slide", 'b--');
for pt in pts:
    x, _ = get_sample(slide_results, pt[0], pt[1], pt[2], xtrace, "Slide");
    y, _ = get_sample(slide_results, pt[0], pt[1], pt[2], ytrace, "Slide");
    points_info.append(((x,y,-15), f"{pt[1]}-Slide", ('s', 'blue')));
    dot_trace[0].append(x);
    dot_trace[1].append(y);
dot_traces.append(dot_trace);



outfile = f"results/plots/Pareto_tradeoff_od_vs_cputime.d{dims[0]}.png";

# Call the function to plot the graph
plot_pareto_curve(points_info, dot_traces, "Quality-Cost Tradeoff Landscape", "Compute Intensity", "Orthogonal Defect ($\Delta$)", outfile);


