import pickle
from plotting import metric_vs_delta


# Load results
results = pickle.load(open("results/BKZ-2024-03-21_09-48-11.pickle", "rb"));

# # Select traces to plot
# dims = [ 8, 16, 32, 64, 128];
# ks = [4];
# deltas = [0.3, 0.5, 0.75, 0.9, 0.99, 0.999, 0.999999];

# outdir = "results/plots"

# metric_vs_delta.plot_delta(results, dims, ks, deltas, outdir);



# Select traces to plot
dims = [ 3, 8, 16, 32, 64, 128];
# dims = [32, 64];
ks = [2, 4, 8, 16, 32];
deltas = [0.99];

outdir = "results/plots"

metric_vs_delta.plot_kappa(results, dims, ks, deltas, outdir);