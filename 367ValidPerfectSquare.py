class ABC : 
    def validSquare (Self,num):
        s,e = 0, num
        while s<=e:
            mid = (s+e)//2
            if mid*mid == num :
                return True
            elif mid*mid >num :
                e = mid-1
            else : 
                s = mid+1
        return False

obj = ABC()
print(obj.validSquare(25))  # Output: (False, None)