from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(maxSum):
            count, currentSum = 1, 0
            for num in nums:
                currentSum += num
                if currentSum > maxSum:
                    count += 1
                    currentSum = num
            return count <= m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left