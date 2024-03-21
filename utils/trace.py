

def KeepGSOBKZFactory(cls):
    """
    Return a wrapper class around ``cls`` which collects Gram-Schmidt norms in the attribute
    ``__KeepGSOBKZ_gso_norms``.

    In particular, the list will be constructed as follows:

    - index 0: input GSO norms
    - index i,j: kappa and GSO norms in tour i-1 for after j-th SVP call
    - index -1: output GSO norms

    :param cls: A BKZ-like algorithm with methods ``__call__``, ``svp_reduction`` and ``tour``.

    .. warning:: This will slow down the algorithm especially for small block sizes.

    """
    class KeepGSOBKZ(cls):
        
        def __init__(self, *args, **kwds):
            cls.__init__(self, *args, **kwds)
            self.__gso_norms = []
            self.__at_toplevel = True
        
        def __call__(self, *args, **kwds):
            self.M.update_gso()
            self.__gso_norms = [self.M.r()]
            self.__at_toplevel = True
            cls.__call__(self, *args, **kwds)
            self.M.update_gso()
            self.__gso_norms.append(self.M.r())

        def svp_reduction(self, kappa, *args, **kwds):
            at_toplevel = self.__at_toplevel
            self.__at_toplevel = False
            r = cls.svp_reduction(self, kappa, *args, **kwds)
            self.__at_toplevel = at_toplevel
            if at_toplevel:
                self.M.update_gso()
                self.__gso_norms[-1].append((kappa, self.M.r()))
            return r

        def tour(self, *args, **kwds):
            if self.__at_toplevel:
                self.__gso_norms.append([])
            clear = cls.tour(self, *args, **kwds);
            if self.__at_toplevel:
                self.M.update_gso()
                self.__gso_norms[-1].append((-1, self.M.r()))
            
            return clear

    return KeepGSOBKZ
