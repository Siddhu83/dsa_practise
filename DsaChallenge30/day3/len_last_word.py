class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        for i in reversed(words):
            if i:
                return len(i)
