### Environments


## Environment Diagram for Nested def Statements
# The parent frame of a func is the frame in which it is defined
# The parent of a frame is the parent of the func called
def make_adder(n):
    def adder(k):
        return n + k
    
    return adder

add_three = make_adder(3)
res = add_three(4)


# Local Names
def f(x, y):
    return g(x) 

def g(a):
    return a + y # when calling g, name y cannot be found in local frame and global frame

f(1, 2)


## Function Composition
def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose_1(f, g):
    def h(x):
        return f(g(x))
    
    return h


## Lambda Expression
# Lambda expressions in python cannot contain statements at all
square = lambda x: x * x


## Function Curring: Transform a multi-arguments func into a single-argument, higher-order func 
from operator import add
# def make_adder(n):
#     return lambda k: n + k

# make_adder(2)(3) # 2 calls
# add(2, 3) # 1 call

def curry_2(f):
    def g(x):
        def h(y):
            return f(x, y)
        
        return h
    
    return g

# Equals to curry_2 = lambda f: lambda x: lambda y: f(x, y)