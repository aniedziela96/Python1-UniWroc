xa = float(input("podaj pierwsza wsplorzedna punktu A: "))
ya = float(input("podaj druga wsplorzedna punktu A: "))
xb = float(input("podaj pierwsza wsplorzedna punktu B: "))
yb = float(input("podaj druga wsplorzedna punktu B: "))

# znaki pierwszych (drugich) wspolrzednych obu punktow musza byc takie
# same aby znajdowaly sie one w tych samych cwiartkach

if xa * xb > 0 and ya * yb > 0:
    print("Punkty ({}, {}), ({}, {}) leza w tej samej cwiartce"
          .format(xa, ya, xb, yb))
else:
    print("Punkty ({}, {}), ({}, {}) nie leza w tej samej cwiartce"
          .format(xa, ya, xb, yb))
