from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []
        for i ,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l , r = i , len(nums)-1 
            while l <r :
                total = a+nums[l]+nums[r]
                if total > 0 : 
                    r -=1
                elif total < 0 :
                    l +=1 
                else :
                    res.append ([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l <r :
                        l +=1

        return res 
    
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))               