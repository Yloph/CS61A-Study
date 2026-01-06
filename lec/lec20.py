### Inheritance



## Inheritance
"""
A method for relating classes together

A common use: Two similar classes differ in their degree of specialization,
the special class may have some general attributes as the general class,
along with some special-case behaviour

class <name>(<base class>):
    <suite>
The subclass may override certain inherited attributes
Implement a subclass by specifying its differences from the base class
"""
class Account:

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient fund"
        self.balance -= amount
        return self.balance

class CheckingAccount(Account):

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)


## Looking up Attributes on Classes
"""
Base class attributes don't copied into subclass
1. If it names a attribute in the class, return the attribute value
2. Otherwise, look up the name in the base class, if there is
"""
ch = CheckingAccount('Tom') # call Account.__init__
ch.interest # Found in CheckingAccount
ch.deposit(20) # Found in Account
ch.withdraw(5) # Found in CheckingAccount


## Object-Oriented Design


## Inheritance and Composition
"""
Inheritance is best for representing is-a relationship
Composition is best for representing has-a relationship
"""
class Bank:
    """
    A bank has accounts

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """
    def __init__(self):
        self.accounts = []
    
    def open_account(self, holder, amount, kind = Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1


## Attributes Lookup Practice
class A:
    
    z = -1
    def f(self, x):
        return B(x - 1)

class B(A):

    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)

class C(B):

    def f(self, x):
        return x

a = A()
b = B(1)
b.n = 5
"""
>>> C(2).n
4
>>> a.z == C.z
True
>>> a.z == b.z
False

Which one evaluates to an integer
b.z # B instance
b.z.z # C instance
b.z.z.z # 1
b.z.z.z.z
"""


## Multiple Inheritance
"""
A class may inherit from multiple base classes
"""
class SavingAccount(Account):

    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(amount - self.deposit_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingAccount):
    
    def __init__(self, account_holder):
        self.balance = 1
        self.holder = account_holder

such_a_deal = AsSeenOnTVAccount('John')
such_a_deal.balance # instance attribute
such_a_deal.deposit(20) # SavingAccount Method
such_a_deal.withdraw(10) # CheckingAccount Method