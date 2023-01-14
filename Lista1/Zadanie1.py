a = - 1  # ustawiam a < 0, aby móc wejść do pętli

while a <= 0:  # Aby program się nie psuł gdy a < 0
    a = float(input("Podaj a > 0: "))
    if a > 0:
        volume = ((a ** 3) * (2 ** (1/2)))/12
        area = (a ** 2) * (3 ** (1/2))
        print("Objetosc: {}".format(volume))
        print("Pole: {}".format(area))
        break
    else:
        print("a musi byc wieksze od 0!")
