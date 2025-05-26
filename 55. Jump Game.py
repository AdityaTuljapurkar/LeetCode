from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0 
        for i in range(len(nums)):
            if i > far :
                return False 
            far = max(far , i+nums[i])
        return True  
nums = [3,2,1,0,4]
s = Solution()
print(s.canJump(nums))