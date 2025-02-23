from typing import List 
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        l =0 
        r =1
        points.sort(key = lambda x: x[1])
        count = 1
        while r < len(points):
            if points[r][0] <= points[l][1]:
                r += 1
            else:
                count += 1
                l =r
                r += 1
        return count
    
points = [[10,16],[2,8],[1,6],[7,12]]
print(Solution().findMinArrowShots(points))