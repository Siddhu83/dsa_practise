def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    trapped = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped += right_max - height[right]

    return trapped