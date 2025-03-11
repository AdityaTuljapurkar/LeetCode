from typing import List 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_len = len(matrix[0])
        row_len = len(matrix) 
        row_index = -1
        for  i in range(row_len) :
            if target == matrix[i][col_len-1]:
                return True 
            if target < matrix[i][col_len-1]:
                row_index= i
                break 
        if row_index == -1 : return False 

        #using binary search for the array    
        l = 0
        r = col_len -1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False 




matrix = [[1,2,4,8]]
target = 3
print(Solution().searchMatrix(matrix,target))
# there is  mouse lost in a chess bord we are assumong that the mouse is starting ti enter in the chess brd form very firest in =dex you need to find a place 
# from where the mouse can come out of chess board to make things simpler the ce]hess bord are replace with 2d mateix wwhich is replaces by 0  and one if the moouse is reaching on zero it wll move forword if it reach at one it will tern 90 digree right   