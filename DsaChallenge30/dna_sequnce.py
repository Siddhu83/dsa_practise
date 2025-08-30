from collections import Counter

class Solution:
    def findRepeatedDnaSequences(s: str) -> list[str]:
        if len(s) < 10:
            return []
        count = Counter()
        res = []
        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            count[seq] += 1
            if count[seq] == 2:
                res.append(seq)
        return res
