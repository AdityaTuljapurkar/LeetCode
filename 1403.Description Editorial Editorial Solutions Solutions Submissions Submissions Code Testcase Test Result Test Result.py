from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        resSum = 0 
        numSum = sum(nums)
        for i in range (len(nums)-1,-1,-1):
            
            if resSum > numSum :
                return res
            
            resSum+=nums[i]
            res.append(nums[i])
            numSum-=nums[i]
            
        return res
nums = [6]
print(Solution().minSubsequence(nums))

            
