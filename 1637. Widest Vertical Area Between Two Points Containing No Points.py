from typing import List
import numpy as np 
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        res:int = 0

        for i in range(1,len(points)):
            res = max(res,(points[i][0])-(points[i-1][0]))

        return res,points 
points = [[8,7],[9,9],[7,4],[9,7]]
sol = Solution()
print(sol.maxWidthOfVerticalArea(points))