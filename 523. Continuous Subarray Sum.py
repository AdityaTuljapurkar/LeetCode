from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0:-1}
        currSum = 0 
        for i , num in enumerate(nums):
            currSum += num
            res = currSum % k
            if res not in rem :
                rem[res]= i
            elif i - rem[res]> 1:
                return True 
        return False
# Test cases
nums = [23, 2, 4, 6, 7]
k = 6
print(Solution().checkSubarraySum(nums,k)) # True
nums = [23, 2, 6, 4, 7]
k = 6
print(Solution().checkSubarraySum(nums,k)) # True
nums = [23, 2, 6, 4, 7]         
k = 13
print(Solution().checkSubarraySum(nums,k)) # False