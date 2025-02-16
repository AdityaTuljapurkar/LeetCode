from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        res = []
        ressult = []
        
        for i in range(1, len(arr)):
            minDiff = min(minDiff, arr[i] - arr[i-1])
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == minDiff:
                res.append(arr[i-1])
                res.append(arr[i])
                ressult.append(res)
                res = []
        
        return ressult

print(Solution().minimumAbsDifference([4,2,1,3]))