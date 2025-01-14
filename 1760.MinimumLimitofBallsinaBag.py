nums = [9]
maxOperations = 2
import math
class ABC():
    def function (self,nums,maxOperations):
        l = 1
        r = max(nums)
        
        def check(mid):
            bags = 0 
            for n in nums :
                bags +=math.ceil(n/mid)-1
                if bags > maxOperations:
                    return False
            return True

        while l <r :
            mid = (l+r)//2
            if check(mid): 
                r = mid 
                
            else : l = mid+1
        return r
    

obj = ABC()
print(obj.function(nums,maxOperations))  