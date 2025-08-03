# the function shall whether given palindrome is valid or not

def is_valid_palindrome(s):
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())

    return normalized_str == normalized_str[::-1]
