def add_vectors(v, w):
    length = len(v)
    v_plus_w = [0] * length
    for i in range(0, length):
        v_plus_w[i] = v[i] + w[i]

    return v_plus_w


print(add_vectors([1, 2, 3, 4], [1, 2, 3, 4]))
