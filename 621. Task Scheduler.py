from typing import List
from collections import Counter  , deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        
        time = 0
        q = deque() 
        while maxheap or q :
            time +=1 
            if maxheap :
                cnt = 1 + heapq.heappop (maxheap)
                if cnt : 
                    q.append([cnt,time+n])
            if q and q[0][1] == time :
                heapq.heappush(maxheap,q.popleft()[0])
        return time 



tasks = ["A","A","A","B","B","B"]
n = 2
sol = Solution()
print(sol.leastInterval(tasks,n))