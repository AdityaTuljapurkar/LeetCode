from typing import List 
class solution  :
    def minDays (Self,bloomDay : List[int],m:int,k:int):
        left = min(bloomDay)
        right = max(bloomDay)
        if len(bloomDay)<m*k :
            return -1
        def validate(mid,k,m):
            count = 0
            for day in bloomDay:
                if day <= mid:
                    count+=1
                    if count == k :
                        m-=1
                        count =0 
                else :
                    count = 0
            # return True if m <= 0 else False
            return m <= 0
        
        while left < right:
            mid  = (left+right)//2
            if validate(mid,k,m):
                right = mid 
            else : 
                left = mid + 1
        return left 




bloomDay = [1,10,3,10,2]
m = 3 
k = 1
sol = solution()
print(sol.minDays(bloomDay,m,k))  # 3  # Output: 3