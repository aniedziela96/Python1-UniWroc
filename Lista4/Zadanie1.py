def fib_iter(n):
    if n < 2:
        return n

    fib = 0
    fib1 = 0
    fib2 = 1
    for i in range(1, n):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib

    return fib


def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_formula(n):
    phi = (1 + (5 ** (1/2))) / 2
    return int(phi ** n / (5 ** (1/2)) + 1/2)


# szukanie tej najmniejszej wartości (zakomentowane, aby przy imporcie
# się nie wykonywało
# n = 1
# while fib_iter(n) == fib_formula(n):
#     n += 1
#
# print(n)
