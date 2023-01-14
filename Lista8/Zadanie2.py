from string import ascii_letters

def count_letters(input_file):
    character_count = {}
    with open(input_file, encoding='utf8') as f:
        for character in f.read():
            if character in ascii_letters:
                character = character.lower()
                character_count[character] = character_count.get(character, 0) + 1
    
    return character_count


def guess_language(input_file, languages):
     
    character_count = sorted(count_letters(input_file).items(), 
                             key = lambda x: x[1], 
                             reverse = True)

    most_commmon_letters = (character_count[0][0], 
                            character_count[1][0], 
                            character_count[2][0])

    for key, value in languages.items():
        if value == most_commmon_letters:
            return key
    
    return "unknown"

if __name__ == "__main__":
    pass