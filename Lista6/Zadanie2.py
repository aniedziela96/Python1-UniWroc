from time import perf_counter
import matplotlib.pyplot as plt

def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


def time_fib(n):
    t0 = perf_counter()
    fib_rec(n)
    t1 = perf_counter()
    return t1 - t0


def fun():
    t1 = time_fib(0)
    t2 = 0
    i = 0
    tab = []
    while t2 <= 3:
        t2 = time_fib(i + 1)
        tab.append(t1/t2)
        t1 = t2
        i += 1
    return tab


if __name__ == "__main__":
    
    tab = fun()
    
    n = range(0, len(tab))

    plt.plot(n ,tab, marker='.', linestyle='None')

    plt.title("ilorazy")
    plt.xlabel("Numer wyrazu ciagu")
    plt.ylabel("Iloraz")

    plt.grid()
    plt.show()