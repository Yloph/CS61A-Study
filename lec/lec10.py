### Tree Recursion


## Order of Recursive Calls
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
# Untill the return value appears, that call has not completed
# Any statement can appear before or after the recursive call

# Another implementation
def cascade_1(n):
    print(n)
    if n >= 10:
        cascade_1(n // 10)
        print(n)

# cascade inverse
def cascade_inverse(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)


## Tree Recursion
"""
Tree-shaped processes arise whenever excuting the body of a recursive
function makes more than one call to that function
"""
from ucb import trace

@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


## Counting Partitions
"""
The number of partitions of a positive integer n, using parts up to size m,
is the number of ways in which n can be expressed as the sum of positive 
positive integer parts up to m in increasing order
"""
@trace
def count_partition(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n - m, m)
        without_m = count_partition(n, m - 1)
        return with_m + without_m