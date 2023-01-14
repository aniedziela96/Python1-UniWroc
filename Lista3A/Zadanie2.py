def sum_digits(n):
    n = str(n)
    s = 0
    for number in n:
        number = int(number)
        s = s + number
    return s


def is_divisible(n):
    if n in [0, 3, 6, 9]:
        return True
    elif n > 10:
        n = sum_digits(n)
        return is_divisible(n)
    else:
        return False


print(is_divisible(12345))
