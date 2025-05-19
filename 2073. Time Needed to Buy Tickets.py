from typing import List 
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count =0 
        val = tickets[k]
        n = len(tickets)
        for i in range(val*n):
            value = tickets[i%n]
            if value > 0 :
                count+=1 
                tickets[i%n] -= 1
                if tickets[i%n] == 0 and i%n == k:
                    return count
        return count
tickets = [2,3,2]
k = 2
print(Solution().timeRequiredToBuy(tickets, k))
tickets = [5,1,1,1]
k = 0
print(Solution().timeRequiredToBuy(tickets, k))