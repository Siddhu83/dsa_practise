def expand_from_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

def find_longest_at_index(s, i):
    start1, end1 = expand_from_center(s, i, i)
    start2, end2 = expand_from_center(s, i, i + 1)
    if end1 - start1 >= end2 - start2:
        return start1, end1
    else:
        return start2, end2

def longest_palindrome(s):
    if len(s) < 2:
        return s
    max_start, max_end = 0, 0
    for i in range(len(s)):
        cur_start, cur_end = find_longest_at_index(s, i)
        if cur_end - cur_start > max_end - max_start:
            max_start, max_end = cur_start, cur_end

    return s[max_start:max_end + 1]
