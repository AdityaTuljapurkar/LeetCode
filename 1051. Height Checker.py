from typing import List 
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = sorted(heights)
        res = 0 
        for i in range(len(arr)):
            if arr[i] != heights[i]:
                res+=1
                
        return res 

heights = [5,1,2,3,4]
sol = Solution()
print(sol.heightChecker(heights))
        