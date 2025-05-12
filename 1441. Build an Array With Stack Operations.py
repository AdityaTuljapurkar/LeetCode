from typing import List 
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        current = 1 
        i = 0 
        while i < len(target):
            if current == target[i]:
                result.append("Push")
                i+=1
            else : 
                result.append("Push")
                result.append("Pop")
            current+=1
        
        return result
    

print(Solution().buildArray([1,3],3))
