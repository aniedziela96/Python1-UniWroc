n = input("Podaj liczbe: ")
suma = 0

for i in n:
    a = int(i)
    if a % 2 != 0:
        suma = suma + a

print(suma)
