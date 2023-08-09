"""
The sum of the primes below 10 is 17.

Find the sum of all the primes below two million
"""


def is_prime(n):
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
    return True


def primer(MAX):
    yield 2
    n = 3
    while n < MAX:
        if is_prime(n):
            yield n
        n += 2


MAX = 2_000_000

primes = primer(MAX)
print(sum(primes))
