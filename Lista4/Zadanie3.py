from math import gcd


def simplify(p, q):
    if q < 0:
        p = -p
        q = -q

    d = gcd(p, q)
    return p // d, q // d


print(simplify(100, -90))
