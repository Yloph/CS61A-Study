### Trees



## Tree Abstraction
"""
Recursive description:
root-label, branch(also a tree), leaf(a tree with 0 branch)

Relative description:
each location in a tree is called node
each node has a label that can be any value
one node can be parent/child of another
"""


## Implementing Tree
def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch), "branches must be tree"

    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list and len(tree) < 1:
        return False
    else:
        for branch in branches(tree):
            if not is_tree(branch):
                return False

    return True

def is_leaf(tree):
    return not branches(tree)


## Tree Processing
def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(t):
    """
    Return a list containing the leaf labels of t

    Hint: if you sum a list of lists, you get a list containing
          the elements of those lists
    """
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(t)], [])

def increment_leaves(t):
    """
    Return a tree like t but with leaf labels inbremented
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    """
    Return a tree like t but with all labels incremented
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment(b) for b in branches(t)]
        return tree(label(t) + 1, bs)


## Printing Trees
def print_tree(t, indent = 0):
    print('  ' * indent, label(t))
    for b in branches(t):
        print_tree(b, indent + 1)


## Summing Paths
numbers = tree(3, [tree(4), tree(5, [tree(6)])])
haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])

def print_sums(t, so_far):
    so_far += label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)


## Count Paths
t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), 
         tree(1, [tree(-1)])])
def count_path(t, total):
    """
    Return the number of paths from the root to any node in
    tree t for which the labels along the path sum to total
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    
    return found + sum([count_path(b, total - label(t)) for b in branches(t)])