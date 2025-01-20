nums = [1,2,1]
class ABC :
    def function(self,nums):
        arr = [0]*(len(nums)*2)
        i = 0
        while i < len(nums):
            arr[i] = nums[i]
            i+=1
        while i < len(arr):
            arr[i] = nums[i-len(nums)]
            i+=1
        return arr
obj = ABC()
print(obj.function(nums))

