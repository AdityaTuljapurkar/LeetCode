import random
class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        res = val not  in self.hashMap 
        if res :
            self.hashMap[val] = len(self.numList)
            self.numList.append(val)
        return res

        
        

    def remove(self, val: int) -> bool:
        res = val in self.hashMap 
        if res :
            index = self.hashMap[val]
            last_value = self.numList[-1]
            self.numList[index] = last_value
            self.numList.pop()
            self.hashMap[last_value] = index 
            del self.hashMap[val]
        return res 
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        