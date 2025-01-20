nums = [1,2,3,4]
class Abc :
    def function(self,nums):
        prefix = [0]*len(nums)
        postfix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = nums[i]*prefix[i-1]
        postfix[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = nums[i]*postfix[i+1]
        output = [0]*len(nums)
        for i in range (0,len(nums)):
            if i == 0:
                output[i] = postfix[i+1]
            elif i ==len(nums)-1:
                output[i] = prefix[i-1]
            else :
                output[i] = prefix[i-1]*postfix[i+1]
            
        return output
            


            
        

            
        
obj = Abc()
print(obj.function(nums))  

        
        
  