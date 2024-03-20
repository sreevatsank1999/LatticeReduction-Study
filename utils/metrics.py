from fpylll import GSO
from math import log

from copy import deepcopy


def orthogonality_defect(B):
    """
    Computes the orthogonality defect of the basis B.
    
    """
    B_= deepcopy(B);
    P = sum([log(B_[i].norm()) for i in range(B_.nrows)])
    
    M = GSO.Mat(B_, update=True);
    
    D = M.get_log_det(0,-1)/2;
    
    defect = P - D;
    return defect