grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]
grid1 = [[3,2],[1,0]]
class ABC : 
    def function(self,grid):
        count = 0
        for  i in range(0,len(grid)):
            for j in range(len(grid[0])-1,-1,-1):
                if grid[i][j] <0:
                    count+=1
        return count

obj  = ABC()
print(obj.function(grid))  # Output: 8
