def Function(nums: list):
    n = len(nums)
    res = [1] * n  

    
    pre = 1
    for i in range(n):
        res[i] = pre
        pre *= nums[i]

    post = 1
    for i in range(n - 1, -1, -1):
        res[i] *= post
        post *= nums[i]

    return res

# Input: nums = [1, 2, 3, 4]
nums=[-1,1,0,-3,3]
print(Function(nums))  # Output: [24, 12, 8, 6]