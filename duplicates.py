# the following functtion will remove the duplicates from a sorted numbers list

def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    unique_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]                
    return unique_index + 1

