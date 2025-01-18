nums = [1,2,3,4]
class ABC():
    def function(self,nums):
        res = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            res.append(sum)
        return res
    
obj = ABC()
print(obj.function(nums))  # [1, 3, 6, 10]