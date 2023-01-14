a = int(input("Podaj liczbe: "))
dzielniki = []  # = 0 dla rozwiazania 1.

# rozwiazanie 1.

# for i in range(1, a + 1):
#     if a % i == 0 and i % 5 != 0:
#         dzielniki += 1
#
# print("Liczba {} ma {} dzielniki(ow) niepodzielnych przez 5"
#       .format(a, dzielniki))

# rozwiazanie przy uzyciu tablicy, na ktorej mamy zapisane dzielniki

for i in range(1, a + 1):
    if a % i == 0 and i % 5 != 0:
        dzielniki.append(i)

print(dzielniki)
print("Liczba {} ma {} dzielniki(ow) niepodzielnych przez 5"
      .format(a, len(dzielniki)))
