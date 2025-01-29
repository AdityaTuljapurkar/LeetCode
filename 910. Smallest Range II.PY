from typing import List
import math 
nums = [1,3,6]
k = 3
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) :
        nums.sort()
        bestL = nums[0] + k
        bestR = nums[-1]-k
        res = nums[-1] - nums[0]

        for i in range(len(nums)-1):
            minVal = min(nums[i+i]-k,bestL) 
            maxVal = max(nums[i]+k,bestR)
            res = min(res,maxVal-minVal)
        return res 
sol = Solution()
print(sol.smallestRangeII(nums, k))  # Output: 3