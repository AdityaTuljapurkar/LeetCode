# Save water Question
import math
def saveWater(nums):
    l =0 
    r =len(nums)-1
    res = - math.inf
    while l<r:
        
        area = (min(nums[l],nums[r]))*(r-l)
        res = max(res,area)
        if nums[l]<nums[r]:
            l+=1
        else : r-=1
    return res


nums =  [1,8,6,2,5,4,8,3,7]
print(saveWater(nums))  # Output: 49