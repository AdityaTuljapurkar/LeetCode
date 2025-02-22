from typing import List 
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break
        return count
print(Solution().maxIceCream([10,6,8,7,7,8] , 7)) #4
                 