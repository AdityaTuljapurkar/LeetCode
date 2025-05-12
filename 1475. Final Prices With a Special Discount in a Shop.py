from typing import List 
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        n = len(prices)
        for i in range(n):
            is_discount  =False             
            for j in range(i+1, n):
                if prices[i]>=prices[j]:
                    result.append(prices[i]-prices[j])
                    is_discount = True 
                    break 
                else :
                    is_discount = False
            if not is_discount :result.append(prices[i])
                     
        return result

print(Solution().finalPrices([8,4,6,2,3]))