from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ts = truckSize
        res =0 
        for i in range (len(boxTypes)):
            if ts == 0 :
                break
            if boxTypes[i][0] <= ts :
                ts-=boxTypes[i][0]
                res+= boxTypes[i][0]*boxTypes[i][1]
            else :
                res+= ts * boxTypes[i][1]
                ts =0
        return res 

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
sol = Solution()
print(sol.maximumUnits(boxTypes,truckSize))