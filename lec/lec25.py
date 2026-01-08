### Data Examples



## List in Environment Diagram
"""
append, extend, addition, slicing 
"""
t = [1, 2, 3]
t[1:3] = [t]
t.extend(t)

t = [[1, 2], [3, 4]]
t[0].append(t[1:2])


## Objects
"""
Instance attributes are found in class attributes
Class attributes are inherited
"""
class Worker:

    greeting = 'Sir'

    def __init__(self):
        self.elf = Worker

    def work(self):
        return self.greeting + ' I work'

    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie:

    greeting = 'Peon'

    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'

Jack = Worker()
John = Bourgeoisie()
Jack.greeting = 'Maam'
"""
>>> Worker.work()

>>> Jack

>>> Jack.work()

>>> John.work()

>>> John.elf.work(John)
"""


## Iterable and Iterators
def min_abs_indices(s):
    min_abs = min(map(abs, s))
    return list(filter(lambda i: abs(s[i]) == min_abs, range(len(s))))
    # return [i for i in range(len(s)) if abs(s[i]) == min_abs]

def largest_adj_sum(s):
    # return max([s[i] + s[i + 1] for i in range(len(s) - 1)])
    return max([a + b for a, b in zip(s[:-1], s[1:])])

def digit_dict(s):
    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}

def all_have_an_equal(s):
    # return all([s[i] in s[:i] + s[i + 1:] for i in range(len(s))])
    return min([s.count(x) for x in s]) > 1


## Linked List
class Link:

    empty = () # some 0-length sequence

    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def ordered(s, key = lambda x: x):
    if s == Link.empty or s.rest == Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)

def merge(s, t):
    if s == Link.empty:
        return t
    elif t == Link.empty:
        return s
    elif s.first < t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))

def merge_in_place(s, t):
    if s == Link.empty:
        return t
    elif t == Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t