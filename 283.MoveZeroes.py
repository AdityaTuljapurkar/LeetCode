nums = [0,0]
class ABC :
    def function(self,nums):
        # move all non zersos towars left
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0 :
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            else : 
                j+=1
        return nums

obj = ABC()
print(obj.function(nums))  
