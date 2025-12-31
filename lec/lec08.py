### Function Examples


## Example 1
def delay(arg):
    print('delayed')
    def g():
        return arg
    return g

# What will be diplayed
delay(delay)()(6)()
print(delay(print)()(4))

## Example 2
from operator import add, mul
def square(x):
    return mul(x, x)

def pirate(arggg):
    print('matey')
    def plunder(arggg):
        return arggg
    return plunder

# What will be displayed
add(pirate(3)(square)(4), 1)
pirate(pirate(pirate))(5)(7)  # type: ignore

## Example 3
def horse(mask):  # type: ignore
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)

# What will be displayed
horse(mask)


## Implement Functions
def remove(n, digit):
    """
    >>> remove(231, 3)
    21
    >>> remove(243213, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        last, n = n % 10, n // 10
        if last != digit:
            kept += 1
            digits += pow(10, kept - 1) * last

    return digits