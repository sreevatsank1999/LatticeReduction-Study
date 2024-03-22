import datetime

import fpylll
from fpylll import *
from fpylll.tools.compare import compare_bkz, setup_logging, BKZFactory, qary30

import algorithms

import pickle

def qary128(dimension, block_size):
    return {"algorithm": "qary",
            "k": dimension//2,
            "bits": 128,
            "int_type": "mpz"}


nbSample = 3        # number of samples
dims = [ 3, 8, 16, 32, 64, 128]          # dimension of the lattice

seed = 2**61 - 1;       # Mersenne prime (M61) as seed
# seed = 42;       

# Parameters 
LLL_delta = 0.99;       # LLL reduction parameter   

BKZ_delta = [0.99];       # BKZ reduction parameter   
BKZ_kappa = [2, 4, 8, 16, 32];          # BKZ reduction parameter   

# BZK_max_loops = 1000;                 # BKZ max reduction iterations
BKZ_tours = 35;                     # BKZ tours

# construct a map of all parameter combinations
# param_map = [(i,j) for i in BKZ_delta for j in BKZ_kappa]

# classes = [];
# for d in BKZ_delta:       
#     BKZ_d = BKZFactory(f"BKZ-d{d}", algorithms.BKZWrapper)
#     # BKZ_d = BKZFactory(f"SDBKZ-d{d}", algorithms.SDBKZWrapper, delta=d)
#     # BKZ_d = BKZFactory(f"Slide-d{d}", algorithms.SlideWrapper)
#     classes.append(BKZ_d)
    
algo = "sdbkz";
d= BKZ_delta[0];
if algo == "bkz":
    BKZcls = BKZFactory(f"BKZ-d{d}", algorithms.BKZWrapper, flags=BKZ.NO_LLL);
    exp_name="BKZ"          # experiment name
elif algo == "sdbkz":
    BKZcls = BKZFactory(f"SDBKZ-d{d}", algorithms.SDBKZWrapper, flags=BKZ.SD_VARIANT);
    exp_name="SDBKZ"          # experiment name
elif algo == "slide":
    BKZcls = BKZFactory(f"Slide-d{d}", algorithms.SlideWrapper, flags=BKZ.SLD_RED);
    exp_name="Slide"          # experiment name
else:
    raise ValueError("Invalid algorithm")

classes = [BKZcls];

setup_logging(exp_name,verbose=True)

results = compare_bkz(classes=classes,
                      matrixf=qary128,
                      dimensions=dims,
                      progressive_step_size=None,
                      block_sizes=BKZ_kappa,
                      samples=nbSample,
                      tours=BKZ_tours,
                      threads=1,
                      seed=seed,
                      logger=exp_name,
                      pickle_jar=None)

# date time in human readable format
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"results/{exp_name}-{now_str}.pickle"
pickle.dump(results, open(filename, "wb"))