from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2 :
            return nums[0]
        
        nums.sort()
        val =0 
        K = N//2
        for i in range(1,N):
            if nums[i-1] == nums[i]:
                val+=1
            else :val = 0 
            if val > K :
                return nums[i]
        return nums[i]

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))