nums = [1,2,3,4,3]
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = []
        n = len(nums)
        for i in range(n*2-1,-1,-1):
            current = nums[i%n]
            while stack and stack[-1] <= current :
                stack.pop()
            #to store only the elemts of the orginal loop 
            if i< n :
                result.append(stack[-1]if stack else -1)
            stack.append(current)
        return result[::-1]
    
sol = Solution()
print(sol.nextGreaterElements(nums))
    
