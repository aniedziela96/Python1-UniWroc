def totient(n):
    m = 0
    for i in range(1, n):
        for j in range(1, n):
            if (i*j) % n == 1:
                m += 1
                break
    return m


print(totient(10))
