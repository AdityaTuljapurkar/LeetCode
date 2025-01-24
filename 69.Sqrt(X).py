class ABC :
    def function (self,x):
        l = 0 
        r = x
        res = 0 
        while l <= r:
            mid = (l+r)//2
            if mid * mid < x:
                l = mid + 1
                res = mid
            elif mid * mid > x:
                r = mid-1
            else :
                return mid
        return res

obj = ABC()
print(obj.function(16))