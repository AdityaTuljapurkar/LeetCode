from collections import defaultdict
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start = defaultdict(int)
        end = defaultdict(int)
        freq= defaultdict(int)
        for i, num in enumerate(nums):
            if num not in start:
                start[num] = i
                end[num] = i
                freq[num] = 1
            else:
                end[num] = i
                freq[num] += 1
            #claculating the value of the degree
        degree = max(freq.values())
        #calculating the length of the subarrayx
        minLen = float('inf')
        for i in freq :
            if freq[i] == degree :
                minLen = min(minLen,(end[i]-start[i])+1)
            
        return minLen

nums = [1,2,2,3,1]
sol = Solution()
print(sol.findShortestSubArray(nums))
                
        
            