def inverse(sigma):
    inverse_perm = [0] * len(sigma)
    for index, value in enumerate(sigma):
        inverse_perm[value] = index

    return inverse_perm


def composition(sigma1, sigma2):
    new_perm = [0] * len(sigma1)
    for index, value in enumerate(sigma2):
        new_perm[index] = sigma1[value]

    return new_perm


print(composition([2, 0, 1, 3], [1, 2, 3, 0]))

