from typing import List
def commonPrefix(str1, str2):
    common = ''
    for i in zip(str1, str2):
        if i[0] != i[1]:
            return common
        common += i[0]
    return common

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in range(1, len(strs)):
            common = commonPrefix(common, strs[i])
        return common
