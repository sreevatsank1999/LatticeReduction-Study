from fpylll import *
from math import *
import numpy as np

from utils import *

A = IntegerMatrix(100,100);
A.randomize("uniform",bits=128);

# print(A)

delta = orthogonality_defect(A);
print("Orthogonality defect of A: ", delta)

M = GSO.Mat(A, update=True);

L = LLL.Reduction(M);
L();

delta = orthogonality_defect(A);
print("Orthogonality defect of LLL(A): ", delta)
