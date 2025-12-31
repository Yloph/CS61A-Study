### Containers


## Box and Pointers


## Slicing
odds = [3, 5, 7, 9, 11]
[odds[i] for i in range(1, 3)]

odds[1 : 3] # -> [1, 3)
odds[: 3] # -> [0, 3)


## Processing containers' values
# Sequence aggregation

# sum(iterable[, start]) -> value
sum([2, 4, 3]) # 2 + 4 + 3
sum([2, 4, 3], 5) # 2 + 4 + 3 + 5
sum([[2, 4], [], [3]]) # [2, 4] + [] + [3] -> [2, 4, 3]

# max(iterable[, key = func]) -> value
# Return the largest item applied to func
max(0, 1, 2, 3, 4) # -> 4
max(range(5)) # -> 4
max(range(10), key = lambda x: 7 - (x - 4) * (x - 2)) # -> 3

# all(interable) -> bool
# Return True if every element of iterable is True else return False
l = [1, 2, 3, 4]
all(l)


## Strings
# Represent data
# Represent language

# len
city = "Berkeley"
len(city)
# substrings
'here' in "where is he" # -> True


## Dictionaries: key -> val
numerals = {'I': 1, 'V': 5, 'X': 10}
numerals['I']
# dic_name.values() -> get valuse of dic_name
numerals.values() # -> dict_values([1, 5, 10])
"""
Restrictions of dictionary keys:
1. cannot be a list or dictionary or any mutable type
2. two keys cannot be equal
"""


## Dictionary comprehension
# {<key>: <val> for <name> in <iter> if <filter exp>}
{x * x: x for x in [1, 2, 3, 4, 5] if x > 2}

def index(keys, values, match):
    """
    keys: a sequence of keys
    values: a sequence of values
    match: a two-arguments func that return bool value

    return a dictionary

    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}