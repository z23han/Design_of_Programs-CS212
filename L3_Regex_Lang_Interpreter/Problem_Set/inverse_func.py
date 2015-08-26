# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negative numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negative numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        epsilon = 0.0000001
        x = y / 2.0
        cnt = 0
        while True:
            df = 2.0*x
            x2 = x - (f(x) - y) / df
            if abs(x2 - x) <= epsilon:
                break
            else:
                x = x2
                cnt += 1
        print cnt
        return x
    return f_1

def square(x): return x*x

import time

if __name__ == '__main__':
    sqrt = slow_inverse(square)
    sqrt2 = inverse(square)
    start_time = time.time()
    print sqrt(1000000000)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    start_time2 = time.time()
    print sqrt2(1000000000)
    elapsed_time2 = time.time() - start_time2
    print(elapsed_time2)