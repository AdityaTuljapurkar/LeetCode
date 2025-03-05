from typing import List 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        while r  < len(nums):
            if nums[l] == nums[r]:
               r+=1
            else : 
                nums[l+1] = nums[r]                
                l+=1
                r+=1
        
        return nums




nums = [0,0,1,1,1,2,2,3,3,4]

print(Solution().removeDuplicates(nums))