from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = -1
        
        for key in nums:
            if key > 0 and -key in hash_set:
                res =  key
        return res
nums = [-9,-43,24,-23,-16,-30,-38,-30]
sol = Solution()
print(sol.findMaxK(nums)) # 3