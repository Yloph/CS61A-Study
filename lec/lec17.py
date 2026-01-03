### Generators



## Generator: a special kind of iterator, returned from a generator func
## Generator Functions: use yield keyword to return value
def plus_minus(x): # can yield multiple times
    yield x
    yield -x

t = plus_minus(3)
next(t) # 3
next(t) # -3


def evens(start, end):
    even = start + start % 2
    while even < end:
        yield even
        even += 2


## Generator can yield from iterator
def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
        """
        for x in coutdown(k - 1):
            yield x
        """
    else:
        yield 'Blast off'
    
for k in countdown(5):
    print(k)


def prefixes(s):
    if s: 
        yield from prefixes(s[:-1]) # not include the last element
        yield s


def substring(s):
    if s:
        yield from prefixes(s)
        yield from substring(s[1:])



## Partitions
def list_partition(n, m):
    """
    Return a list of lists
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partition(n - m, m)]
        without_m = list_partition(n, m - 1)
        return exact_match + with_m + without_m


def partition(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in partition(n - m, m)]
        without_m = partition(n, m - 1)
        return exact_match + with_m + without_m


def yield_partition(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in yield_partition(n - m, m):
            yield p + ' + ' + str(m)
        yield from yield_partition(n, m - 1)