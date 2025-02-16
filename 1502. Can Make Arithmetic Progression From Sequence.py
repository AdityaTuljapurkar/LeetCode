from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) == 2:
            return True
        diff =  arr[1]-arr[0]

        for i in range(2,len(arr)):
            if arr[i]-arr[i-1] != diff:
                return False

        return True 

print(Solution().canMakeArithmeticProgression(arr = [1,2,4])) 