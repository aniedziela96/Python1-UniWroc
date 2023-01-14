from Zadanie1 import fib_rec
from time import perf_counter


def time_fib(n):
    t0 = perf_counter()
    fib_rec(n)
    t1 = perf_counter()
    return t1 - t0


def fun():
    t2 = 0
    i = 0
    while t2 <= 5:
        t1 = time_fib(i)
        t2 = time_fib(i + 1)
        print(t2/t1)
        i += 1
