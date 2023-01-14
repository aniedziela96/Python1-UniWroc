import palindrome

def palindromes_file(file):
    new_file = open('palindromy.txt', 'a')
    with open(file) as file1:
        for word in file1:
            if palindrome.is_palindrome(word.strip()):
                new_file.write(word)
        
    new_file.close

if __name__ == "__main__":
    palindromes_file('collins2015.txt')

