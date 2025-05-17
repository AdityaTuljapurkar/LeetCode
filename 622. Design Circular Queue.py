class LinkedListNode: 
    def __init__(self,value,pre,next):
        self.value , self.pre,self.next = value,pre,next 


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k 
        start = LinkedListNode(0,None,None)
        end = LinkedListNode(0,None,None)
        start.next = end 
        end.pre= start  
        self.start = start
        self.end = end
        self.count =0 

    def enQueue(self, value: int) -> bool:
            if self.isFull():
                return False 
            newNode = LinkedListNode(value,self.end.pre,self.end) 
            self.end.pre.next = newNode 
            self.end.pre = newNode 
            self.count += 1 
            return True 
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 
        self.start.next = self.start.next.next 
        self.start.next.pre = self.start 
        self.count -= 1 
        return True 

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.start.next.value 

    def Rear(self) -> int:
        if self.isEmpty():
            return -1 
        return self.end.pre.value         

    def isEmpty(self) -> bool:
        if self.start.next == self.end and self.end.pre == self.start :
            return True 
        return False

    def isFull(self) -> bool:
        if self.size ==  self.count :
            return True 
        return False