from typing import List 
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        #using two pinter with sorting  
        nums.sort()
        i = 0
        j = len(nums) - 1
        max_sum = []
        while i < j:
            max_sum.append(nums[i] + nums[j])
            i += 1
            j -= 1
        return max(max_sum)

print(Solution().minPairSum([3,5,4,2,4,6]))