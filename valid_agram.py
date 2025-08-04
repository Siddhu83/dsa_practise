# this funtion will return the valid agram for the given input
# it will return the valid agram for the given input

def is_anagram(input_str1, input_str2):
    return sorted(input_str1) == sorted(input_str2)
    