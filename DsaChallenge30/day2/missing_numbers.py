class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        total_sum = size * (size + 1) // 2
        return total_sum - sum(nums)