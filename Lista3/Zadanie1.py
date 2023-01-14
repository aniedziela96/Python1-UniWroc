def first_common_character(s1, s2):
    for letter_s1 in s1:
        if letter_s1 in s2:
            return letter_s1


a = input()
b = input()
print(first_common_character(a, b))
