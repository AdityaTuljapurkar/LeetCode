weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

class ABC : 
    def function(self, weights, days):
        
        l = max(weights) #min
        r = sum(weights) #max
        res = sum(weights)
        
        def countDays(mid):
            shift = 1
            curr = mid
            for weight in weights :
                if curr -weight <= 0 :
                    shift += 1
                    curr = mid
                curr -= weight
            return shift <= days 
        
        while l < r: 
            mid = (l + r) // 2
            if countDays(mid) :
                res = min(res,mid)
                r = mid-1
            else : 
                l = mid+1
        return res


obj = ABC()
print(obj.function(weights,days)) # 15

