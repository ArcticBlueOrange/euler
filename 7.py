# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


primes = set()


def isprime(n):
    if n & 1 == 0 and n > 2:
        return False
    for i in primes:
        if i > n >> 1:
            continue
        if n % i == 0:
            return False
    return True


i = 1
n = 2

while True:
    if isprime(n):
        print(f"{i}\t{n}")
        primes.add(n)
        i += 1
        if i >  10_001:
            break
    n += 1

# print(primes)
