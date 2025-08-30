class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [nums[0]]
        size = len(nums)
        for i in range(1, size):
            runningSum.append(runningSum[i - 1] + nums[i])
        return runningSum
        