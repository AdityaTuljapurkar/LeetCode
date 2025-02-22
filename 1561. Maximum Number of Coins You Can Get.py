from typing import List 
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        Sum : int =0
        j =0
        for i in range(n):
            j = 2*i+1
            Sum += piles[j]
            if i == len(piles) // 3:
                break
        return Sum 

print(Solution().maxCoins([2,4,1,2,7,8]))


        