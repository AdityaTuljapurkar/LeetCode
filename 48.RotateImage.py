matrix = [[1,2,3],[4,5,6],[7,8,9]]
class ABC :
    def function(self,matrix):
        l = 0
        r  = len(matrix)-1
        while l < r :
            for i in range(r - l):
                t = l 
                b = r
                # storing tempery value
                topLeft = matrix[t][l+i]
                #for the  left element
                matrix[t][l+i] =matrix[b-i][l]
                #for the bottom element
                matrix[b-i][l] = matrix[b][r-i]
                #for the right element
                matrix[b][r-i] = matrix[t+i][r]
                #for the top element
                matrix[t+i][r] = topLeft    
            r -= 1
            l += 1
        return matrix

obj = ABC()
print(obj.function(matrix))  

