### Composition



## Linked List
"""
A linked list is either empty or the first value and rest of the linked list
"""
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


## Linked List Processing
square = lambda x: x * x
odd = lambda x: x % 2 == 1

def range_link(start, end):
    """
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))

def map_link(f, l):
    """
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if l == Link.empty:
        return l
    else:
        return Link(f(l.first), map_link(f, l.rest))

def filter_link(f, l):
    """
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if l == Link.empty:
        return l
    else:
        if f(l.first):
            return Link(l.first, filter_link(f, l.rest))
        else:
            return filter_link(f, l.rest)


## Linked List Mutation
s = Link(1, Link(2, Link(3, Link.empty)))
s.first = 5
t = s.rest
t.rest = s

# evaluate to what
s.first # 5
s.rest.rest.rest.rest.rest.first # 2


## Linked List Mutation Example
def add(v, s):
    """
    add v to an ordered Link s with no repeats, returning modified s
    if v is already in s, return s itself without modify

    >>> s = Link(1, Link(3, Link(5)))
    >>> add(0, s)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(3, s)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(4, s)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(6, s)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    assert s != Link.empty

    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest == Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(v, s.rest)
    return s


## Tree Class
class Tree:

    def __init__(self, label, branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)
    
    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])

def leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves

def height(t):
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])

def prune(t, n):
    """
    Prune all sub-trees whose label is n
    """
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)