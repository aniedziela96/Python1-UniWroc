def run_length_encoding(lista):
    short_lst = []
    n = 1
    character = lista[0]
    for i in range(1, len(lista)):
        if lista[i] == character:
            n += 1
        else:
            short_lst.append((character, n))
            n = 1
            character = lista[i]
    short_lst.append((character, n))
    return short_lst

def run_lenght_uncoding(lista):
    long_list = []
    for character, n in lista:
        i = 0
        while i < n:
            long_list.append(character)
            i+=1

    return long_list


if __name__ == "__main__":
    a = ['a', 'a', 'a', 'c', 'r', 'r', 'r', 'r', 'i']
    b = run_length_encoding(a)
    c = run_lenght_uncoding(b)
    print(b)
    print(c)
