matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
class ABC : 
    def function(self,matrix):
        r = len(matrix[0])
        b = len(matrix)
        l = 0
        t = 0
        row  = False
        col = False 
        for  i in range(l , r):
            if matrix[t][i] == 0 :
                row = True
        for j in range(t,b):
            if matrix[j][l] == 0 :
                col = True
        
        for  i in range(t+1,b):
            for j in range(l+1,r) :
                if matrix[i][j] == 0 :
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range (t+1,b):
            for j in range(l+1,r):
                if matrix[i][0]== 0 or matrix[0][j]==0 :
                    matrix[i][j] = 0

        if row  : 
            for i in range(0,r):
                matrix[0][i] = 0
        if col :
            for i in range(0,b):
                matrix[i][0] = 0
        
        return matrix 

obj = ABC()
result = obj.function(matrix)  # [[0,0,0],[0,0,0],[
for row in result :
    print(row)  # [0, 0, 0], [0, 0

