
import fpylll
from fpylll import *
from fpylll.tools.compare import compare_bkz, setup_logging, BKZFactory, qary30

import fpylll.algorithms.bkz

import pickle

nbSample = 3        # number of samples
dims = [3, 8, 16, 32, 64, 128]          # dimension of the lattice

seed = 2**61 - 1;       # Mersenne prime (M61) as seed

# Parameters 
LLL_delta = 0.99;       # LLL reduction parameter   

BKZ_delta = [0.3, 0.5, 0.75, 0.9, 0.99, 0.999, 0.999999];       # BKZ reduction parameter   
BKZ_kappa = [2, 4, 8, 16];          # BKZ reduction parameter   
BZK_max_loops = 1000;                 # BKZ max reduction iterations
BKZ_tours = 100;                     # BKZ tours

# construct a map of all parameter combinations
# param_map = [(i,j) for i in BKZ_delta for j in BKZ_kappa]

classes = [];
for d in BKZ_delta:
    BKZ_d = BKZFactory(f"BKZ-d{d}", fpylll.algorithms.bkz.BKZReduction, delta=d, max_loops=BZK_max_loops)
    classes.append(BKZ_d)
    

exp_name="BKZ-convergence"          # experiment name

setup_logging(exp_name,verbose=True)

results = compare_bkz(classes=classes,
                      matrixf=qary30,
                      dimensions=dims,
                      progressive_step_size=None,
                      block_sizes=BKZ_kappa,
                      samples=nbSample,
                      tours=BKZ_tours,
                      threads=1,
                      seed=seed,
                      logger=exp_name,
                      pickle_jar=None)


pickle.dump(results, open(f"results/{exp_name}.pickle", "wb"));
