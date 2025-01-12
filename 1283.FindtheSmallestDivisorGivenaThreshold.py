import math 
nums = [1,2,5,9]
threshold = 6
def function (nums:list[int], threshold:int):
    s , e = 0, len(nums)-1
    result = nums[e] 
    while s< e :
        mid = (s+e)//2
        sum = 0
        for i in nums : 
            sum += math.ceil(i)/nums[mid]
        if sum <= threshold : 
            result = nums[mid] 
            e = mid-1
        elif sum > threshold :
            s = mid+1
    return result
            
            
    
print(function (nums,threshold))
        
