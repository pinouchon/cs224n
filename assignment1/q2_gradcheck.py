#!/usr/bin/env python

import numpy as np
import random


# First implement a gradient checker by filling in the following functions
def gradcheck_naive(f, x):
    """ Gradient check for a function f.

    Arguments:
    f -- a function that takes a single argument and outputs the
         cost and its gradients
    x -- the point (numpy array) to check the gradient at
    """

    rndstate = random.getstate()
    random.setstate(rndstate)
    
############### WARNING ###################
# fx, grad = f(x)is a VERY STUPID notation.
# Never do that, whatever your religion is. 
###########################################

    fx, grad = f(x) # Evaluate function value at original point
    h = 1e-4        # Do not change this!

    # Iterate over all indexes in x
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    import copy
    while not it.finished:   
        ix = it.multi_index   
        xitp = copy.deepcopy(x)

        xitp[ix] = xitp[ix] + h


        xitm = copy.deepcopy(x)
        xitm[ix] = xitm[ix] - h
       
        random.setstate(rndstate)          
        fxitp = f(xitp)[0]
        
        random.setstate(rndstate)
        fxitm = f(xitm)[0]

        numgrad = (fxitp - fxitm)/(2*h)

        # Compare gradients
        reldiff = abs(numgrad - grad[ix]) / max(1, abs(numgrad), abs(grad[ix]))
        if reldiff > 1e-5:
            print "your gradient: %f \t Numerical gradient: %f" % (
                grad[ix], numgrad)
        #else: print('OK')

        it.iternext() # Step to next dimension

    print "Gradient check passed!"


def sanity_check():
    """
    Some basic sanity checks.
    """
    quad = lambda x: (np.sum(x ** 2), x * 2)

    print "Running sanity checks..."
    gradcheck_naive(quad, np.array(123.456))      # scalar test
    gradcheck_naive(quad, np.random.randn(3,))    # 1-D test
    gradcheck_naive(quad, np.random.randn(4,5))   # 2-D test
    print ""


def your_sanity_checks():
    """
    Use this space add any additional sanity checks by running:
        python q2_gradcheck.py
    This function will not be called by the autograder, nor will
    your additional tests be graded.
    """
    print "Running your sanity checks..."


if __name__ == "__main__":
    sanity_check()
    your_sanity_checks()
