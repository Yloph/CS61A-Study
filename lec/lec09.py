### Recursion

## Self-reference: A func can refer its own name within its body
#  example 1
def print_all(x):
    print(x)
    return print_all

print_all(1)(3)

# example 2
def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x + y)
    return next_sum

print_sums(1)(3)(5)


## Recursive Functions: The body of a func that calls it self
# Sum digits without using a while statement
def split(n):
    return n // 10, n % 10

def sum_digits_without_while(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return last + sum_digits_without_while(all_but_last)

sum_digits_without_while(2013)

# Iteration is a special type of recursion


## Mutual Recursion: Two different funcs call each other
# Example: The Luhn Algorithm
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits_without_while(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit