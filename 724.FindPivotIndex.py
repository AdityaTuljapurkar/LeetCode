nums = [1,7,3,6,5,6]
class ABC :
    def function(self,nums):
        numSum = sum(nums)
        # pivort = 0 
        left  = 0 
        right = numSum
        for pivort in range(0,len(nums)):
            right -= nums[pivort]
            if left == right:
                return pivort
            left += nums[pivort]
        return -1
    
obj = ABC()
print(obj.function(nums))  # Output: 3