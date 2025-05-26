class RecentCounter:

    def __init__(self):

        self.queue = [] 

    def ping(self, t: int) -> int:
        counter = 0
        self.queue.append(t)
        i = len(self.queue) - 1
        while self.queue and i >=0 and self.queue[i]>=(t-3000):
            counter +=1 
            i-=1 
        return counter
        
rc = RecentCounter()
assert rc.ping(1) == 1     # [1]
assert rc.ping(100) == 2   # [1, 100]
assert rc.ping(3001) == 3  # [1, 100, 3001]
assert rc.ping(3002) == 3  # [100, 3001, 3002]
