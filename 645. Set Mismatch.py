from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        hashset = set()
        n = len(nums)     
        result = []                                                                                                          
        for i in range(n):
            if nums[i] in hashset:
                result.append(nums[i])
            else:
                hashset.add(nums[i])
        for i in range(1, n + 1):
            if i not in hashset:
                result.append(i)
                break
        return result
        
# Test the function
sol = Solution()
nums = [1, 2, 2, 4]
result = sol.findErrorNums(nums)
print(result)  # Output: [3, 2]
