# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def get_factors(number):
    if number <= 1:
        return
    d = 2
    while d <= number:
        rem = number % d
        if rem:
            d += 1
            continue
        yield d
        number = number // d


# print([x for x in get_factors(16)])
# print([x for x in get_factors(13195)])

print([x for x in get_factors(600851475143)])
print(max(x for x in get_factors(600851475143)))
