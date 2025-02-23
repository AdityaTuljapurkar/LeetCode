from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using count sort  
        maxNum = max(nums)+1 
        count = [0]*maxNum
        for i in nums:
            count[i] += 1
        j=0
        for i in range(maxNum):
            while count[i]> 0 :
                nums[j] = i
                j += 1
                count[i] -= 1
        return nums
#Time complexity: O(n)
#Space complexity: O(n)     
print(Solution().sortColors([2,0,2,1,1,0]))

