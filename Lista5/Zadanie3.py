def pearson_corr(lst1, lst2):
    if len(lst1) != len(lst2):
        return None
    else:
        n = len(lst1)
        x_ = (1 / n) * sum(lst1)
        y_ = (1 / n) * sum(lst2)

        arr1 = []
        arr2 = []
        arr3 = []
        for i in range(0, n):
            arr1.append((lst1[i] - x_) * (lst2[i] - y_))
            arr2.append((lst1[i] - x_)**2)
            arr3.append((lst2[i] - y_)**2)

        return sum(arr1) / ((sum(arr2) ** (1 / 2)) * (sum(arr3) ** (1 / 2)))


print()
