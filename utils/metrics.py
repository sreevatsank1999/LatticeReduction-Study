from fpylll import GSO, LLL
from math import log

from copy import deepcopy


def orthogonality_defect(B):
    """
    Computes the orthogonality defect of the basis B.
    
    Returns: log(defect)
    """
    B_= deepcopy(B);
    P = sum([log(B_[i].norm()) for i in range(B_.nrows)])
    
    M = GSO.Mat(B_, update=True);
    
    D = M.get_log_det(0,-1)/2;
    
    defect = P - D;
    return defect

def hermite_factor(B):
    """
    Computes the Hermite factor of the basis B. Assume B is LLL-reduced.
    
    Returns: log(Hf)
    """
    
    if not LLL.is_reduced(B):
        raise ValueError("Basis B is not LLL-reduced.")
    
    B_= deepcopy(B);
    M = GSO.Mat(B_, update=True);

    d = M.d;
    
    V = M.get_log_det(0,-1)/2;
    
    Hf = log(B[0].norm()) - V/d;
    
    return Hf

