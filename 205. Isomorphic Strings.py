class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        hashS = {}  
        hasht = {}  
        
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            if charS in hashS:
                if hashS[charS]!= charT:
                    return False
    
            elif charT in hasht:
                if hasht[charT]!=charS:
                    return False
            else :
                hashS[charS] = charT
                hasht[charT] = charS
        return True
# Test cases        
s = "egg"
t = "add"
print(Solution().isIsomorphic(s,t)) # True
s = "foo"
t = "bar"
print(Solution().isIsomorphic(s,t)) # False
            