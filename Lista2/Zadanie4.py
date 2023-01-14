a = ''
tabl = []
iloczyn = 1

while True:
    a = input()
    if a != 'end':
        a = float(a)
        tabl.append(a)
    else:
        break

if len(tabl) == 0:
    print("Error")
else:
    for i in tabl:
        iloczyn = iloczyn * i

    srednia_geom = iloczyn ** (1/len(tabl))
    print(srednia_geom)
