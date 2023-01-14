from string import ascii_uppercase

def caesar(text, n):
    alphabet = ascii_uppercase
    caesar_text = ''
    for character in text:
        if character in alphabet:
            i = alphabet.find(character)
            caesar_text = caesar_text + alphabet[(i + n) % len(alphabet)]
        else:
            caesar_text = caesar_text + character

    return caesar_text

def uncaesar(text, n):
    caesar(text, -n)
    # alphabet = ascii_uppercase
    # uncaesar_text = ''
    # for character in text:
    #     if character in alphabet:
    #         i = alphabet.find(character)
    #         uncaesar_text = uncaesar_text + alphabet[(i - n) % len(alphabet)]
    #     else:
    #         uncaesar_text = uncaesar_text + character

    # return uncaesar_text

if __name__ == "__main__":
    print(uncaesar('ALH. LHYS NYLF. OVA', 7))

