from typing import List 
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack =  []
        i = 0
        for num in pushed : 
            stack.append(num)
            while i < len(popped) and stack and stack[-1]== popped[i]:
                i+=1
                stack.pop()
        return not stack
    
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(Solution().validateStackSequences(pushed,popped))
