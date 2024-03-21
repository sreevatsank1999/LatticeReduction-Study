import datetime

import fpylll
from fpylll import *
from fpylll.tools.compare import compare_bkz, setup_logging, BKZFactory, qary30
from fpylll.tools.bkz_plot import KeepGSOBKZFactory

import fpylll.algorithms.bkz

import pickle

nbSample = 1        # number of samples
dims = [64]          # dimension of the lattice

seed = 2**61 - 1;       # Mersenne prime (M61) as seed

# Parameters 
LLL_delta = 0.99;       # LLL reduction parameter   

BKZ_delta = [0.99];       # BKZ reduction parameter   
BKZ_kappa = [16];          # BKZ reduction parameter   
# BZK_max_loops = 1000;                 # BKZ max reduction iterations
BKZ_tours = 100;                     # BKZ tours

# construct a map of all parameter combinations
# param_map = [(i,j) for i in BKZ_delta for j in BKZ_kappa]

# BKZcls = BKZFactory("GSO-BKZ", KeepGSOBKZFactory(fpylll.algorithms.bkz.BKZReduction));
BKZcls = KeepGSOBKZFactory(fpylll.algorithms.bkz.BKZReduction);


exp_name="SDBKZ-convergence"          # experiment name

A = IntegerMatrix(dims[0], dims[0])
# A.randomize("uniform", bits=50)
# A.randomize("simdioph", bits=30, bits2=50)
# A.randomize("intrel", bits=64)
A.randomize("qary", bits=128, k=dims[0]//2)

bkz = BKZcls(A);

params = BKZ.Param(block_size=BKZ_kappa[0],flags=BKZ.SD_VARIANT)

for i in range(BKZ_tours):
    bkz.tour(params);

# date time in human readable format
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"results/{exp_name}-{now_str}.pickle"
pickle.dump({"gso_norms": bkz._KeepGSOBKZ__gso_norms, "blocksize": BKZ_kappa[0]}, open(filename, "wb"))