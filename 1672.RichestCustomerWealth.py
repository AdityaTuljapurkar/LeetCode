accounts = [[1,2,3],[3,2,1]]
class ABC:
    def function(self,accounts):
        maxSum = 0
        for i in range( len(accounts)):
            Sum = 0
            for j in range( len(accounts[0])):
                Sum += accounts[i][j]
                maxSum = max(maxSum,Sum)
        return maxSum
obj = ABC()
print(obj.function(accounts))