from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        l  , r = 0 , 1 
        maxProfit = 0
        #using kadane's algorithm
        while r < len(prices):
            if prices [l] < prices[r]:
                maxProfit = max(maxProfit,prices[r]-prices[l])
            else : 
                l = r 
            r += 1
        return maxProfit
# Test cases    
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices)) # 5