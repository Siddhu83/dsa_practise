# this function will rturn a list of list containing gropued anagrams

def sort_str(my_str):
    return ''.join(sorted(my_str))

def group_anagrams(strs):
    anagrams_dict = {sort_str(s): [] for s in strs}
    for i in strs:
        c = sort_str(i)
        anagrams_dict[c].append(i)
    
    return list(anagrams_dict.values())

