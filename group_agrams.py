# this function will rturn a list of list containing gropued anagrams

def sort_str(my_str):
    return ''.join(sorted(my_str))

def group_anagrams(strs):
    anagrams_dict = {}
    for i in strs:
        c = sort_str(i)
        if c not in anagrams_dict:
            anagrams_dict[c] = [i]
        else:
            anagrams_dict[c].append(i)
    
    return list(anagrams_dict.values())

