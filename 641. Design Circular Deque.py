class LinkedListNode:
    def __init__(self,value,pre,next):
        self.value , self.pre, self.next = value,pre,next 
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k 
        start = LinkedListNode(0,None,None)
        end = LinkedListNode(0,None,None)
        start.next = end 
        end.pre= start  
        self.start = start
        self.end = end
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = LinkedListNode(value,self.start,self.start.next)
        self.start.next.pre = newNode 
        self.start.next = newNode
        self.count += 1 
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = LinkedListNode(value,self.end.pre,self.end)
        self.end.pre.next = newNode
        self.end.pre = newNode 
        self.count += 1 
        return True 
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False 
        self.start.next = self.start.next.next
        self.start.next.pre = self.start 
        self.count -=1 
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False 
        self.end.pre = self.end.pre.pre
        self.end.pre.next = self.end 
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.start.next.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.end.pre.value 

    def isEmpty(self) -> bool:
        if self.start.next == self.end and self.end.pre == self.start:
            return True 
        return False

    def isFull(self) -> bool:
        if self.size == self.count:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()