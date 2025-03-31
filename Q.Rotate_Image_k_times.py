from typing import List
class Solution:
    # Function to rotate the matrix by 90 degrees clockwise.
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transposing matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversing each row
        for i in range(n):
            l = 0
            r = n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
        return matrix

        # Function to rotate the matrix by 90 degrees clockwise.
    def RotateKTimes(self,nums:List[int],k:int) -> List[int]:
        k%=4
        for i in range(k):
            self.rotate(matrix)
        return matrix
# Example usage:
#
    
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
k = 3
obj = Solution()
print(obj.RotateKTimes(matrix,k)) 
