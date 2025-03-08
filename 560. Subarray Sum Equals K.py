from typing import List 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        res= 0
        Sum =0 
        for num in nums :
            Sum += num
            diff = Sum-k
            res += freq.get(diff,0)
            if Sum in freq :
                freq[Sum] += 1
            else : 
                freq[Sum] = 1
        return res
nums = [1,-1,1,1]
k = 3
print(Solution().subarraySum(nums,k))