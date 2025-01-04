nums = [2,7,11,15,23,15]
target = 9

class ABC : 
    def function (self,nums,target):
        hashMap = {}
        for i, n in enumerate(nums):
            deff = target-n
            if (deff) in hashMap:
                return [hashMap[deff],i] 
            hashMap[n]=i    
        return 
obj = ABC()
print(obj.function(nums,target))