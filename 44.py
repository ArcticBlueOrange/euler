
def pentagonals(nth):
    n = 1
    for n in range(1,nth):
        yield int(n * (3*n-1) / 2)


pents = pentagonals(10)
for p in pents:
    print(p)
