# The sum of the squares of the first ten natural numbers is,
#  1**2 + 2 ** 2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1+2+3....+10) **2 = 55**2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# print(sum(i ** 2 for i in range(11)))
# print(sum(range(10+1))**2)

sumsquares = sum(i ** 2 for i in range(101))
squaressum = sum(range(101)) ** 2

print(sumsquares, squaressum, squaressum - sumsquares)
