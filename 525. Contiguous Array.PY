from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero , one = 0 , 0 
        hashTable = {}# to store diff of 0 and 1 
        res = 0 

        for i , num in enumerate(nums):
            if num == 0:
                zero += 1 
            else:
                one += 1 
            diff = zero - one 
            if diff not in hashTable:
                hashTable[diff] = i
            if one == zero :
                res = max(res , one + zero)
            else :
                index = hashTable[diff]
                res = max(res , i - index)  
        return res
# Test cases
nums = [0,1]
print(Solution().findMaxLength(nums)) # 2
nums = [0,1,0]
print(Solution().findMaxLength(nums)) # 2
nums = [0,1,0,1]
print(Solution().findMaxLength(nums)) # 4