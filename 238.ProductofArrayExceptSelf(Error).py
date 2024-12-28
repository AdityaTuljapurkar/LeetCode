# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
nums = [1,2,3,4]

def Function(nums:list):
    j = len(nums)-1
    i = 0 
    ptr = 0 
    post = 1
    pre  = 1 
    res= []
    while i < len(nums):
        if ptr == 0 : 
            pre = 1 
            
        else : 
            pre = nums[ptr-1]*pre
            pre = pre*nums[i-1]
        res[ptr]= pre
        ptr+=1
        i+=1
           
    while j > 0 : 
        if ptr == len(nums)-1 :j-=1
        else : 
            post =post * res[j]
            res[j]= post 
            j-=1
    return res
print(Function(nums))
            
            





        
