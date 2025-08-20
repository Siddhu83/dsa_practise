def maxSlidingWindow(nums, k):
    maxList = []
    for i in range(len(nums) - k + 1):
        maxList.append(max(nums[i : i + k]))
    return maxList
    