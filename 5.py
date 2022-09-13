# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


from functools import reduce


def divbyall(num, divs):
    for i in divs:
        if num % i != 0:
            return False
    return True


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


def factors_in_range(max):
    ret = {}
    for i in range(2, max+1):
        f = [x for x in get_factors(i)]
        tmp = {x: f.count(x) for x in f}
        for k, v in tmp.items():
            if ret.get(k, 0) < v:
                ret[k] = v
    return ret


# print(divbyall(10, [2, 3,  5]))
# print([x for x in get_factors(20)])
# print(factors_in_range(20))
# print([k ** v for k, v in factors_in_range(20).items()])
print(reduce(lambda a, b: a * b,
      [k ** v for k, v in factors_in_range(20).items()]))
