import math
nums =[1,1]
x = 3
class Solution:
    def minOperations(self, nums, x: int) -> int:
        Sum = sum(nums)
        val = Sum- x
        if Sum <x:
            return -1
        start = 0
        total = 0
        count = 0
        minLen = (math.inf)
        N = len(nums)

        for end in range(N):
            total += nums[end]
            while total > val:
                total -= nums[start]
                start += 1
            if total == val:
                count = N-(end -start +1)
                minLen = min(minLen,count)
        return -1 if minLen == math.inf else minLen
solution = Solution()
print(solution.minOperations(nums,x))
