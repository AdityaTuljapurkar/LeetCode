from typing import List 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res =  []
        maxVal = max(abs(i) for i in nums)+1
        count = [0]*(maxVal)
        for i in nums :
            count[abs(i)] += 1 
        
        for i in range(maxVal):
            while count[i] > 0 :
                res.append(i*i)
                count[i]-=1
        
        return res
    
nums = [-1]
sol = Solution()
print(sol.sortedSquares(nums))
