import numpy
original = [1,2]
m = 1
n = 1
class ABC : 
    def function(self,original,m, n):
        if len(original)!= m*n: return []
        else :
            z = 0 
            arr = [[0 for _ in range(n)]for _ in range(m)]
            for i in range (m):
                for j in range (n):
                    arr[i][j] = original[z]
                    z+=1
            return arr

obj = ABC()         
print(obj.function(original,m,n))