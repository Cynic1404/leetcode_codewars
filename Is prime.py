"""Is Prime

Define a function isPrime that takes one integer argument and returns true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Example

isPrime(5)
=> true"""

def is_prime(x):
    if x<2:
        return False
    elif x == 2 or x == 3:
        return True
    else:
        for n in range(2, x-1):
            if x%n==0:
                return False
        else:
            return True