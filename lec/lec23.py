### Efficiency



## Measure Efficiency
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# decorator function
def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted


## Memoization
"""
Remember the results that have been computed before
"""
def memo(f):
    cache = {} # keys are argument that map to return values
    def memorised(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorised # same behavior as f, if f is a pure function


## Exponentiation
def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n - 1)

def exp_fast(b, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return exp_fast(b, n // 2) * exp_fast(b, n // 2)
    else:
        return b * exp_fast(b, n - 1)


## Order of Growth Notation


## Orders of Growth


## Space
# Active Frames