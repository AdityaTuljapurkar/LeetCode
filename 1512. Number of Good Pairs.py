from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        hashMap = {}
        for num in nums:
            if num in hashMap:
                count += hashMap[num]
                hashMap[num] += 1
            else : 
                hashMap[num] = 1
        return count

nums = [1,2,3,1,1,3]
s = Solution()
print(s.numIdenticalPairs(nums))