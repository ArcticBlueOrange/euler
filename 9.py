"""
A Pythagorean triplet is a set of three natural numbers,
a < b < c , for which, a**2+b**2=c**2

For example, 
.

There exists exactly one Pythagorean triplet for which 
a + b + c = 1000
Find the product abc

"""
from pprint import pprint

isquare = lambda x: int(x**.5) == x**.5

def istriplet(a,b,c):
    return a**2 + b**2 == c**2

def tripler(a,b):
    c = ((a**2) + (b**2) )**.5
    if c == int(c):
        return int(c)
    return None

triplets = []
for a in range(1,1000):
    for b in range(1,a):
        c = tripler(a,b)
        if c:
            triplets.append(
                {
                    'a':a,
                    'b':b,
                    'c':c,
                    's':sum([a,b,c]),
                    'p':a*b*c,
                }
                )

# find triplets 
# pprint(triplets)
pprint([t for t in triplets if t['s'] == 1000])
