import math 
nums = [1,2,5,9]
threshold = 6
def function (nums:list[int], threshold:int):
    s , e = 1, max(nums)
    while s < e:
        mid = (s+e)//2
        sum = 0
        for num in nums:
            sum += math.ceil(num/mid)
        if sum <= threshold:
            e = mid 
        
        else : 
            s = mid +1
    return s

            
    
print(function (nums,threshold))
