class Solution:
    def smallestSubsequence(self, s: str) -> str:
        #hashmap :
        lastIndex = [0]*26 
        for i,c  in enumerate(s) :
            lastIndex[ord(c)-ord('a')] = i
        stack =  []
        seen = set()
        for i , c in enumerate(s):
            if c in seen : 
                continue

            while stack and c < stack[-1] and lastIndex[ord(stack[-1])-ord('a')] > i :
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)
        return ''.join(stack)
# Test