n = int(input("Podaj n: "))
x = float(input("Podaj x z przedzialu (-1, 1): "))
y = 1
suma = 0

for k in range(1, n + 1):
    y = y * (-x)
    suma = suma + ((-1) * (y/k))

print(suma)
