import math
piles = [3,6,7,11]
h = 8
class ABC :
    def function(self,piles,h):
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (l+r)//2
            Hrs = 0
            for  i in piles :
                Hrs += math.ceil(i/mid)
            if Hrs <= h :
                res = min(res,mid)
                r = mid-1
            else : 
                l = mid+1
        return res
obj = ABC()
print(obj.function(piles,h))
    

        