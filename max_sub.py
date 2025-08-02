# the following funtion will return the maximum subarray sum

def max_sub(input_array):
    if not input_array:
        return 0
    max_sum = input_array[0]
    for i in range(len(input_array)):
        current = 0
        for j in range(i, len(input_array)):
            current += input_array[j]
            if current > max_sum:
                max_sum = current
    return max_sum