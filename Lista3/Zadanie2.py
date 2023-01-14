def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def first_divisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    else:
        return 0


def is_semi_prime(n):
    d = first_divisor(n)
    if d != 0:
        if is_prime(n // d) == 1:
            return True
    return False


def next_semi_prime(n):
    while True:
        if is_semi_prime(n + 1) == 1:
            return n + 1
        else:
            n += 1


def print_semi_prime(k):
    # i = 1
    # j = 1
    # while i <= k:
    #     if is_semi_prime(j) == 1:
    #         print(j)
    #         i += 1
    #     j += 1

    semi_prime = next_semi_prime(1)
    for i in range(1, k + 1):
        semi_prime = next_semi_prime(semi_prime)
        print(semi_prime)


print(is_semi_prime(56))
