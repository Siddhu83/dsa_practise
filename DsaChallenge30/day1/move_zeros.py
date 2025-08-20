class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroInd = 0
        for i in range(len(nums)):
            if nums[i]: #checking for a non-zero number
                nums[nonZeroInd], nums[i] = nums[i], nums[nonZeroInd]
                # swapped the zero with non-zero element
                nonZeroInd += 1 
        