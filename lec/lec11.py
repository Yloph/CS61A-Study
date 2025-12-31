### Sequences
from operator import add, mul, getitem

## Lists
digits = [2, 8, 1, 8]

# The number of elements
len(digits)
# An element selected by index
digits[2]
getitem(digits, 2)
# Concatenation and repetition
[2, 7] + 2 * digits
add([2, 7], mul(2, digits))
# Nested lists
pairs = [[1, 2], [3, 4]]
pairs[1]
pairs[1][0]


## Containers
digits = [1, 8, 2, 8]

# Built-in operator to test whether an element appears in a compound value
# in operator looks for individual element
1 in digits
5 in digits


## For statements
def count(s, val):
    """
    Count the number of times val appears in sequence s
    """
    ans = 0
    for elem in s:
        if elem == val:
            ans += 1
    
    return ans

# Sequence unpacking in for statement
def same_count(s):
    ans = 0
    for x, y in s:
        if x == y:
            ans += 1
    
    return ans 

pairs = [[1, 2], [2, 2], [3, 4], [4, 4]]
same_count(pairs)


## Ranges: a sequence of consecutive integers
# range(-2, 2) -> [-2, 2)
range(-2, 2)
range(4) # range with a 0 starting value -> [0, 4)
# convert range to list
list(range(-2, 2))

def sum_below(n):
    ans = 0
    for i in range(n):
        ans += i
    
    return ans



## List comprehension
odds = [1, 3, 5, 7, 9]
[x + 1 for x in odds]
[x for x in odds if 25 % x == 0]

def divisor(n):
    return [1] + [x for x in range(2, n) if n % x == 0]