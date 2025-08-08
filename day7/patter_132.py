def find132pattern(nums):
    stack = []
    possible_middle = nums[-1]
    for index in range(len(nums) - 1, -1, -1):
        current = nums[index]
        if current < possible_middle:
            return True
        while stack and current > stack[-1]:
            possible_middle = stack.pop()
        stack.append(current)
    return False