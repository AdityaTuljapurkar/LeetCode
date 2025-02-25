                  
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        t = 0
        b = 1
        res = []
        output = []
        
        intervals.sort(key = lambda x: x[0])
        

        res.append(intervals[0][0])
        
        while b < len(intervals):
            if intervals[b][0] <= intervals[t][1]:

                intervals[t][1] = max(intervals[t][1], intervals[b][1])
                b += 1
            else:

                res.append(intervals[t][1])
                output.append(res)

                res = []
                res.append(intervals[b][0])  
                t = b
                b += 1
        

        res.append(intervals[t][1])
        output.append(res)
        
        return output

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))
