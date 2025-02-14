from typing import List 
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res= nums[0]
        
        i =2
        while i <= len(nums)-2 :
            res+=nums[i]
            i +=2

        return res
nums = nums = [6,2,6,5,1,2]
sol =Solution()
print(sol.arrayPairSum(nums))