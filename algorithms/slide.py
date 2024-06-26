
from time import process_time  # Python 3

from fpylll import IntegerMatrix, GSO, LLL
from fpylll import BKZ
from fpylll import Enumeration
from fpylll import EnumerationError
from fpylll.util import adjust_radius_to_gh_bound
from fpylll.tools.bkz_stats import dummy_tracer, normalize_tracer, Tracer


class SlideWrapper(object):
    """
    Wrapper around the Slide algorithm from fplll C++. This class is used to collect statistics
    """

    def __init__(self, A):
        """Construct a new instance of the BKZ algorithm.

        :param A: an integer matrix, a GSO object or an LLL object

        """
        if isinstance(A, GSO.Mat):
            L = None
            M = A
            A = M.B
        elif isinstance(A, LLL.Reduction):
            L = A
            M = L.M
            A = M.B
        elif isinstance(A, IntegerMatrix):
            L = None
            M = None
            A = A
        else:
            raise TypeError("Matrix must be IntegerMatrix but got type '%s'" % type(A))
        
        self.A = A
        if M is None:
            self.M = GSO.Mat(A, flags=GSO.ROW_EXPO)
        else:
            self.M = M
        if L is None:
            self.lll_obj = LLL.Reduction(self.M, flags=LLL.DEFAULT)
        else:
            self.lll_obj = L
        
        self.M.discover_all_rows();
        self.M.update_gso();
        
               
        self._i =0;
        params = BKZ.Param(block_size=2, flags=BKZ.DEFAULT)
        self._core = BKZ.Reduction(self.M, self.lll_obj, params)
        
        # WARNING: This is a hack. We should not have to call the HKZ postprocessing
        # self.num_rows = self._core.nodes;
        self.num_rows = self.A.nrows;
        
    def tour(self, params, min_row=0, max_row=-1, tracer=dummy_tracer):
        """One BKZ loop over all indices.

        :param params: BKZ parameters
        :param min_row: start index ≥ 0
        :param max_row: last index ≤ n

        :returns: ``True`` if no change was made and ``False`` otherwise
        """
        if max_row == -1:
            max_row = self.A.nrows

        self.sld_potential = self.M.get_slide_potential(0,self.num_rows,params.block_size);
        
        with tracer.context("tour",self._i):
            clean  = self._core.slide_tour(self._i, params, min_row, max_row)
            self.M.update_gso()
            
            clean &= self.hkz_postprocessing(params, tracer)
        
        self._i += 1;
        return clean

    def hkz_postprocessing(self, params, tracer=dummy_tracer):
        """One HKZ postprocessing step.

        :param params: BKZ parameters
        :param tracer: a tracer object

        :returns: ``True`` if no change was made and ``False`` otherwise
        """
        clean = True;
        
        # hkz reduce the blocks (which are otherwise only svp and dual svp reduced)
        p = self.num_rows // params.block_size
        if self.num_rows % params.block_size:
            p += 1
        for j in range(p):
            kappa = j * params.block_size + 1
            end = min(self.num_rows, kappa + params.block_size - 1)
            (clean_, kappa_max_) = self._core.hkz(params, kappa, end)
            clean &= clean_

        return clean