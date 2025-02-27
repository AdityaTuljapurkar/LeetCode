from typing import List 
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) :
        
        nums = [str(i) for i in nums]
        def compare(nums1,nums2):
            return -1 if nums1 + nums2 > nums2 + nums1 else 1 

        nums.sort(key=cmp_to_key(compare))
        if nums[0]== "0":
            return "0"
            
        return "".join(nums)
    
nums = [10,2]

print(Solution().largestNumber(nums))
