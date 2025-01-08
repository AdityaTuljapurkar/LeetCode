# Output: true
# Explanation: Any triplet where i < j < k is valid.
import math
nums = [2,1,5,0,4,6]
class abcd :                                                                            
    def function(self,nums):
        arr= [math.inf]*3
        # for r in range(3):
        #     arr[r] = math.inf
            
        arr[0] = min(arr[0],nums[0])
        i=1
        while i < len(nums):
            if arr[0] > nums[i]:
                arr[0] = min(nums[i],arr[0])
            elif arr[0] < nums[i] and arr[1] > nums[i]:
                arr[1] = min(arr[1],nums[i])
            elif arr[0] < nums[i] and arr[1] < nums[i] and arr[2] > nums[i]:
                arr[2] = min(arr[2],nums[i])
            i+=1
        return False if arr[2] == math.inf else True
            
        
obj = abcd ()
print(obj.function(nums))
 
        
               