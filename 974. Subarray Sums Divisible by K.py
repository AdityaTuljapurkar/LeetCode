from typing import List 
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
            freq = {0:1}
            res =0 
            Sum = 0 
            Val = -1
            for num in nums : 
                Sum += num
                Val = Sum %k
                res += freq.get(Val,0)
                freq[Val] = freq.get(Val,0)+1
            return res
nums = [4,5,0,-2,-3,1]
k = 5
print(Solution().subarraysDivByK(nums,k))   
