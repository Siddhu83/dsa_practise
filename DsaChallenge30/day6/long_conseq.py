# leetcode 128: longest_conseqqutive-sequence
from typing import List

class Solution:
    def longest_consecutive(nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:  # start of sequence
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest