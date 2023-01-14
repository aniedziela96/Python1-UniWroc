def print_conversion_table(start, step, count):
    print("{0:^10} \t | {1:^30} \t | {2:^20}"
          .format("kg/m^3", "t/in^3", "lb/ft^3"))
    print("-" * 70)

    for i in range(start, (count * step) + start, step):
        a = (i * (0.001 / 61024.7))
        b = i * (2.2 / 35.3)
        print("{0:^10} \t | \t {1:^.25f} \t | \t {2:^20f}".format(i, a, b))


print_conversion_table(23, 15, 11)

