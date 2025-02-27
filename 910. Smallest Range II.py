from typing import List 
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) :
        nums.sort()
        bestL = nums[0]+k
        bestR = nums[-1]-k 
        res = nums[-1]- nums[0]

        for i in range(len(nums)-1):
            minVal = min(bestL , nums[i+1]-k)
            maxVal = max(bestR,nums[i]+k)
            res=  min (res,maxVal-minVal)

        return res 
print(Solution().smallestRangeII([1,3,6],3))