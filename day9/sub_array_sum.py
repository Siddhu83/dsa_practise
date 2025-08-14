#leetcode question 560: subarray sum equals k

def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    cumulative_sum = 0
    sum_map = {0: 1}  # Initialize with sum 0 having one occurrence
    
    for num in nums:
        cumulative_sum += num
        
        # Check if (cumulative_sum - k) exists in the map
        if cumulative_sum - k in sum_map:
            count += sum_map[cumulative_sum - k]
        
        # Update the map with the current cumulative sum
        if cumulative_sum in sum_map:
            sum_map[cumulative_sum] += 1
        else:
            sum_map[cumulative_sum] = 1
            
    return count