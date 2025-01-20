mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
class ABC :
    def funtion(self,mat):
        primaryDialgonal = 0 
        secoundaryDiagonal = 0
        for i in range(len(mat)):
            primaryDialgonal += mat[i][i]
            secoundaryDiagonal += mat[i][len(mat)-i-1]
        return primaryDialgonal + secoundaryDiagonal - (mat[len(mat)//2][len(mat)//2] if len(mat)%2 !=0 else 0)

obj = ABC()
print(obj.funtion(mat))