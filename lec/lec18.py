### Object



## Object-oriented Programing
"""
A method to organize program
A metapher for computation using distributed state

class, object, method
"""


## CLass Statement
class Account:
    def __init__(self, account_holder): # a special function that constructs a class instance
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount): # self is a instance of Account on which deposit is invoked by dot expression
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance


## Creating Instances
a = Account('Alan')
a.balance = 12 # the value of an attribute can be changed

b = Account('Bob')
b.balance = 20
a.backup = b # a new attribute that wasn't named before can be added


## Object Identity
## Invoking Methods(by using dot expression)