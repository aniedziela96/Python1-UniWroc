from math import factorial, e, fabs
import matplotlib.pyplot as plt

def frange(start, final, step=1.0):
    result = []
    while start < final:
        result.append(start)
        start = start + step
    return result

def e1(n):
    tab = []
    for i in range(0, n + 1):
        tab.append(1/factorial(i))
    return sum(tab)

def e2(n):
    if n == 1:
        return 1
    tab = []
    for i in range(0, n + 1):
        tab.append((-1)**i/factorial(i))
    return 1/sum(tab)

def wykres(n):
    x = range(1,n)
    xs = range(0,n)
    e1 = [1/factorial(0)]
    e2 = [(-1)**0/factorial(0)]
    for i in x:
        e1.append((1/factorial(i) + e1[i - 1]))
        e2.append((-1)**i/factorial(i) + e2[i - 1])

    for i in range(0,n):
        if i == 1:
            e2[i] = e - 1
            e1[i] = fabs(e - e1[i])
        else:
            e1[i] = fabs(e - e1[i])
            e2[i] = fabs(e - 1/e2[i])

    return e1, e2, xs
   



if __name__ == "__main__":


    tab_error1, tab_error2, x = wykres(30)
    
    plt.plot(x, tab_error1, marker = '.', linestyle='solid')
    plt.plot(x, tab_error2, marker = '.', linestyle='solid')

    plt.title("Przyblizenia liczby e")
    plt.xlabel("Błąd bezwzględny")
    plt.ylabel("Liczba sumowanych wyrazów w rozwinięciu Taylora")
    plt.legend(["przyblizenie 1", "przyblizenie 2"])
    plt.yscale('log')  # 'log' for logarythmic

    plt.grid()
    plt.show()