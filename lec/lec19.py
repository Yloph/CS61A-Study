### Attributes



## Class Attributes
class Account:

    interest = 0.02 # part of Account class

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return 'Insufficient fund'
        self.balance -= amount
        return self.balance

tom_account = Account('Tom')
jim_account = Account('Jim')
tom_account.interest # interest is not part of instance


## Attribute Lookup
"""
Both inatance and class have attributes that can be looked up by dot expression

<expression>.<name>:
1. Evaluate the <expression> to the left of the dot, which yields the object of the dot expression
2. <name> is matched against the instance attributes of that object;
   if an attribute with that name exists, its value is returned
3. If not, <name> is looked up in the class, which yields a class attribute value
4. That value is returned unless it is a function, in which case a bound method is returned instead

getattr(instance, <name>)
hasattr(instance, <name>)
"""
getattr(tom_account, 'balance')
hasattr(tom_account, 'deposit')


## Attribute Assignment
"""
If the object is an instance, then assignment sets an instance attribute
If the objece is a class, then assignment sets a class attribute
"""
tom_account = Account('Tom') # adds or modifies the attribute named 'interest' of tom_account
jim_account = Account('Jim')
tom_account.interest = 0.08
jim_account.interest # evaluate to 0.02, not 0.08

Account.interest = 0.04 # class attribute assignment
tom_account.interest # evaluate to instance attribute 0.08
jim_account.interest # evaluate to class attribute 0.04


## Method Calls
a = Account('Alan')
a.deposit # a bound method
a.deposit(10) # method call

## Bound Methods
"""
That are functions and also attributes, 
where the self argument has already been filled in with an instance of class
"""
b = Account('Bob')
type(Account.deposit) # Function
type(b.deposit) # method

Account.deposit(b, 1000) # same as b.deposit(1000)