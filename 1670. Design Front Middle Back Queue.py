from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = deque()

    def pushFront(self, val: int) -> None:
        prev_length = len(self.queue)
        self.queue.append(val) 
        for _ in range(prev_length):
            self.queue.append(self.queue.popleft())


    def pushMiddle(self, val: int) -> None:
        k = len(self.queue) // 2
        if len(self.queue) == 1 or len(self.queue) == 0:
            self.queue.append(val)
        else:      
            for i in range(len(self.queue)):
                if i == k:
                    self.queue.append(val)
                self.queue.append(self.queue.popleft())

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue.popleft()

    # def popMiddle(self) -> int:
    #     k = len(self.queue) // 2
    #     if self.isEmpty():
    #         return -1
    #     elif len(self.queue) ==1 :
    #         return self.queue.popleft()
    #     val =0 
    #     for i in range(len(self.queue)):
    #         if i == k:
    #             val = self.queue[i]
    #             self.queue.remove(val)
    #         else:

    #             self.queue.append(self.queue.popleft())
    #     return val
    def popMiddle(self) -> int:
        if self.isEmpty():
            return -1
    
        k = (len(self.queue) - 1) // 2  # lower middle
        val = 0
    
        # Step 1: Bring the middle element to the front
        for i in range(len(self.queue)):
            x = self.queue.popleft()
            if i == k:
                val = x  # found middle, don't re-add it
            else:
                self.queue.append(x)  # keep rotating
    
        return val


    def popBack(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue.pop()

    def isEmpty(self) -> bool:
        return len(self.queue) == 0