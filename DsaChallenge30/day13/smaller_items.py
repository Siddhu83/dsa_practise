from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}
        for i, value in enumerate(sorted_nums):
            if value not in rank:
                rank[value] = i
        return [rank[num] for num in nums]