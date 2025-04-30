from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i , j = 0, 0
        res =[]
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                res.append([start, end])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res
# Test
if __name__ == "__main__":
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    solution = Solution()
    print(solution.intervalIntersection(firstList, secondList))  # Output: [[1,2],[5,5],[8,10],[15,23],[24,25]]
    firstList = [[1,3],[5,9]]
    secondList = []
    print(solution.intervalIntersection(firstList, secondList))  # Output: []
    firstList = []
    secondList = [[4,8],[10,15]]
    print(solution.intervalIntersection(firstList, secondList))  # Output: []        