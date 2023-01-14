def is_palindrome_iter(it):
    arr = []
    for i in it:
        arr.append(i)
    if it == arr:
        return True
    else:
        return False


print(is_palindrome_iter("kajak"))
