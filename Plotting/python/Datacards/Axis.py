#!/usr/bin/env python
"""
Axis: Helper class for Sparsinator/Categorization
"""

########################################
# Axes
########################################

class axis:
    def __init__(self,
                 name,
                 nbins,
                 xmin,
                 xmax,
                 fun = None,
                 addUnderflow = 0,
                 addOverflow = 0,
                 discPrereq = []
    ):
        """" Defines an axis for a multi-dimensional histogram
        name         : name of the axis
        nbins        : number of bins
        xmin         : lower boundary of axis
        xmax         : upper boundary of axis
        fun          : function to evaluate, will receive a TTree as argument (not stored when pickled!!!)
        addUnderflow : if True - put values into lowest bin instead of underflow
        addOverflow  : if True - put values into highest bin instead of overflow
        discPrereq   : if the axis is used as a discriminator variable
                         (so MEM/BDT instead of nJets) then this should
                         hold a list of Cut objects corresponding to
                         minimal cut for it to be well defined.
        """

        self.name         = name
        self.nbins        = nbins
        self.xmin         = xmin
        self.xmax         = xmax
        self.fun          = fun
        self.addUnderflow = addUnderflow
        self.addOverflow  = addOverflow
        self.discPrereq   = discPrereq
        

    def __repr__(self):
        return "axis object: {0} with {1} bins, range: {2}..{3}".format(self.name,
                                                                        self.nbins,
                                                                        self.xmin,
                                                                        self.xmax)

    def __getstate__(self):
        odict = self.__dict__.copy() # copy the dict since we change it
        del odict['fun']             # remove function entry
        return odict

    def __setstate__(self, dict):
        self.__dict__.update(dict)   # update attributes
        self.__dict__["fun"] = None


# end of class axis        
