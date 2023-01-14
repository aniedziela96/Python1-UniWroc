def get_primes(n):
    primes = list(range(2, n + 1))
    for i in primes:
        for j in reversed(primes):
            if j != i:
                if j % i == 0:
                    primes.remove(j)
            else:
                break

    return primes


print(get_primes(100))
