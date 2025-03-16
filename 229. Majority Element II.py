from typing import  List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        if N == 0:
            return []
        n = N//3
        freq = {}
        res = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for key in freq:
            if freq[key]> n:
                res.append(key)
        return res
sol = Solution()   
nums = [3,2,3]
print(sol.majorityElement(nums)) #[3]
nums = [1]
print(sol.majorityElement(nums)) #[1]
nums = [1,2]
print(sol.majorityElement(nums)) #[1,2]
nums = [1,2,3]
print(sol.majorityElement(nums)) #[]
nums = [1,1,1,3,3,2,2,2]
print(sol.majorityElement(nums)) #[1,2]