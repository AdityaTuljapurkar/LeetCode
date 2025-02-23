from typing import List 
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()

        Sum = 1
        for coin in coins:
            if coin > Sum :
                break
            
            Sum += coin
            
        return Sum
    


coins =[1,1,1,4]
print(Solution().getMaximumConsecutive(coins))

