nums = [1,12,-5,-6,50,3]
k = 4
class ABC():
    def function(self,nums,k):
        curr =0 
        for i in range(k):
            curr += nums[i]
        maxAvg = curr/k
        for i in range(k, len(nums)):
            curr += nums[i]
            curr -= nums[i-k]
            avg = curr/k
            maxAvg = max(maxAvg,avg)
        return maxAvg

obj = ABC()
print(obj.function(nums,k))  # Output: 12


            