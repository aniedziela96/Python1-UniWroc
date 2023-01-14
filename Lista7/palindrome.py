def is_palindrome(s):
    length = len(s)
    for i in range(0, (length//2)+1):
        if s[i] != s[length - 1 - i]:
            return False

    return True


if __name__ == "__main__":
    pass

