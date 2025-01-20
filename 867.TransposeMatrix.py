matrix =[[1,2,3],[4,5,6]]
class ABC  :
    def function(self,matrix):
        output  = [[0 for _ in range(len(matrix))]for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                output[j][i]= matrix[i][j]
        return output
obj = ABC()
print(obj.function(matrix))