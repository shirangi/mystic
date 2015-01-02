#!/usr/bin/env python
# ******NOTICE***************
# optimize.py module by Travis E. Oliphant
#
# You may copy and use this module as you see fit with no
# guarantee implied provided you keep this notice in all copies.
# *****END NOTICE************
#
# Forked by: Mike McKerns (February 2009)
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2009-2015 California Institute of Technology.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/mystic/browser/mystic/LICENSE
""" local copy of scipy.optimize.linesearch """

def line_search(f, myfprime, xk, pk, gfk, old_fval, old_old_fval,
                args=(), c1=1e-4, c2=0.9, amax=50):

    try: #XXX: break dependency on scipy.optimize.linesearch
        from scipy.optimize import linesearch
        alpha_k, fc, gc, old_fval, old_old_fval, gfkp1 = \
                         linesearch.line_search(f,myfprime,xk,pk,gfk,\
                         old_fval,old_old_fval,args,c1,c2,amax)
    except ImportError:
        alpha_k = None
        fc = 0
        gc = 0
        gfkp1 = gfk #XXX: or None ?

    return alpha_k, fc, gc, old_fval, old_old_fval, gfkp1

