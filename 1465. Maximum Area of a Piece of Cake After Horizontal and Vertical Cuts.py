from typing import List
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        maxH = 0
        maxW = 0
        for i in range(1,len(horizontalCuts)):
            maxH = max(maxH,horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1,len(verticalCuts)):
            maxW = max(maxW,verticalCuts[i]-verticalCuts[i-1])
        return (maxH*maxW)%(10**9+7)
    
print(Solution().maxArea(5,4,[1,2,4],[1,3]))