def largestNumber(nums):
    nums = list(map(str, nums))
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] + nums[i] > nums[i] + nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    if nums[0] == "0":
        return "0"

    return "".join(nums)
