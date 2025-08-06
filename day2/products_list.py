# this function returns a list of products of all elements in the input list except the element at the current index.

def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    prefix_product = suffix_product = 1
    for i in range(n):
        answer[i] = prefix_product
        prefix_product *= nums[i]

    for i in range(n - 1, -1, -1):
        answer[i] *= suffix_product
        suffix_product *= nums[i]

    return answer