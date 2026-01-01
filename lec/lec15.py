### Mutability


## Object
"""
Object represent information
They consists data and behavior, bundled together to create abstraction
Object can represent things but also properties, interactions and processing
A type of a object is called class(first-class value in Python)

Object-oriented programming

In Python, every value is a object
"""
from datetime import date # date is a class


## String
s = 'Hello'
s.upper() # do not change value of s
s.lower()

from unicodedata import name, lookup
name('a')
name('A')
lookup('SNOWMAN')
lookup('SOCCER BALL')


## Mutation Operation
"""
The same object can change in value throught the course of computation
All names that refer to the same object are affected by a mutation

Object of mutable type: list and dictionary

A func can change the value of any object within its scope
"""
# list
suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop() # remove the last element and return it
suits.remove('string') # remove the specific element
suits.append('cup') 
suits.extend(['sword', 'club'])
suits[2] = 'spade'
suits[0 : 2] = ['heart', 'diamond']
# dictionary
numerals = {'I': 1, 'V': 5, 'X': 10}
numerals['X'] = 11
numerals['L'] = 50
numerals.pop('X')


## Tuple: immutable sequences
"""
A immutable value may still change if it contains 
a mutable value as element
"""
s = ([1, 4], 3)
s[0][0] = 4 # s[0] = 4 -> Error


## Identity Operation
a = [10]
b = [10]
a == b # True
a is b # False

c = b
c == b # True
c is b # True

c.append(10)
a.append(20)
c == b # True
c is b # True

# Mutable default arguments are dangerous
def f(s = []):
    s.append(5)
    return len(s)

f() # -> 1
f() # -> 2
f() # -> 3


## Mutable Functions
def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] -= amount
        return b[0]
    
    return withdraw

withdraw = make_withdraw_list(100)
withdraw(25)