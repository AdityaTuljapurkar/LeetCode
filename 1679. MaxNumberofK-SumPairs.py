nums = [1,2,3,4]
k=5
class ABC :
    def function(self, nums, k):
        nums.sort()
        count = 0 
        i = 0
        j = len(nums)-1
        while i < j : 
            if (nums[i] + nums[j]) == k :
                count += 1
                i += 1
                j -= 1
            elif (nums[i] + nums[j-1]) < k :
                i +=1
            elif (nums[i] + nums[j-1]) > k :
                j -= 1
        return count
obj = ABC()
print(obj.function(nums,k))
