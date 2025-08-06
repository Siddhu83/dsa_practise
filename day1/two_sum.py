def two_sum(input_array, target):
    left = 0, right = len(input_array) - 1 
    while left < right:
        current_sum = input_array[left] + input_array[right]
        if current_sum == target:
            return (input_array[left], input_array[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    if result:
        print(f"Two numbers that add up to {target} are: {result}")
    else:
        print(f"No two numbers add up to {target}")