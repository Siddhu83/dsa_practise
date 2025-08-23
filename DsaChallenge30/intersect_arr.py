from collections import Counter
class Solution:
    def intersect(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    count = Counter(nums1)
    result = []
    for num in nums2:
        if count[num] > 0:
            result.append(num)
            count[num] -= 1
    return result
