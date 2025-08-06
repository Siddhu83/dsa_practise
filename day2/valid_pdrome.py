# the function shall whether given palindrome is valid or not

def is_valid_palindrome(s):
    redefined = ''.join(char.lower() for char in s if char.isalnum())

    return redefined == redefined[::-1]
