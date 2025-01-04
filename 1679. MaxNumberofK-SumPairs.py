nums = [1,2,3,4]
k = 5
class ABC :
    def function(self, nums, k):
        numsMap = {}
        count = 0
        for index,i in enumerate(nums):
            numsMap[index]= i
        for  i in nums :
            if (k-i) in numsMap.values():
                nums.remove(k-i)
                count+=1
                

        return count
obj = ABC()
print(obj.function(nums,k))
