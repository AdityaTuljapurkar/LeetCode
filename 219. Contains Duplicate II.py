from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        hashMap = {}
        for i , num in enumerate(nums):
            if num in hashMap and abs(hashMap[num]-i) <= k : return True
            hashMap[num] = i
        return False 
        
        

nums = [1,0,1,1]
k = 1
# nums = [1,2,3,1,2,3]
# k = 2
print(Solution().containsNearbyDuplicate(nums,k))