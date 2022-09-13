# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def ispal(number):
    snum = str(number)
    s = 0
    e = len(snum) - 1
    while s < e:
        if snum[s] != snum[e]:
            return False
        s += 1
        e -= 1
    return True


def palmults(min, max):
    f0 = min
    while f0 <= max:
        f0 += 1
        f1 = min
        while f1 <= max:
            res = f0 * f1
            if ispal(res):
                yield res
            f1 += 1


# print([x for x in palmults(10, 99)])
# print(max(x for x in palmults(10, 99)))
# print(max(x for x in palmults(100, 999)))
print(max(x for x in palmults(900, 999)))
