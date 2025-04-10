matrix = [[1,2,3],[4,5,6],[7,8,9]]
class ABC :
    def function(self,matrix):
        res = []
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)

        while left < right and top < bottom:
            for i in range(left,right):
                res.append(matrix[top][i])
            top +=1

            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -=1

            if left > right or top>bottom:
                break

            # if not (left < right and top < bottom):  # Break early if boundaries overlap
            #     break
            
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom -=1
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
                left+=1
        return res

obj = ABC()
print(obj.function(matrix))