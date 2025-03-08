from typing import List 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        j = i+1

        res= []
        ans = []
        for i in range(n-3):
            if nums[i] == nums[i-1] and i > 0 :
                continue 
            for j in range(i+1,n-2):
                if nums[j] == nums[j-1] and j > i+1 :
                    continue 
                l = j+1
                r=  n-1
                while l < r :
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total == target :
                        res.append(nums[i])
                        res.append(nums[j])
                        res.append(nums[l])
                        res.append(nums[r])
                        ans.append(res)
                        res = []
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums [l-1] : l+=1
                        while l < r and nums[r] == nums [r+1] : r-=1 
                    
                    elif total > target :
                        r-=1
                    else : 
                        l +=1 
        return ans
    
nums = [1,0,-1,0,-2,2]
target = 0
print(Solution().fourSum(nums,target))


