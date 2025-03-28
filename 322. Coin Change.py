from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+1)
        dp[0] = 0
        for a in range(1,amount+1):
            dp[a] = amount+1
            for c in coins :
                if a-c >= 0 :
                    dp[a]= min(dp[a],dp[a-c]+1)
        return dp[amount] if dp[amount] != amount+1 else -1
    
print(Solution().coinChange([1,3,4,5],7)) 