kwota_dochodu = float(input("Podaj swoja kwote dochodu: "))

if kwota_dochodu < 8000:
    podatek = 0
elif kwota_dochodu < 34500:
    podatek = 0.1 * (kwota_dochodu - 8000)
else:
    podatek = 0.1 * (34500 - 8000) + 0.24 * (kwota_dochodu - 34500)

print("Twoj podatek wyniosi: {}".format(podatek))
