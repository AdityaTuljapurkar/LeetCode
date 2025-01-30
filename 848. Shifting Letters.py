from typing import List  
class solution :
    def shiftingLetters(self,s:str,shifts : List[int]) -> str :
        n = len(shifts)
        suffix = [0]*n
        suffix[-1] = shifts[-1]
        ans = []
        for i in range (n-2,-1,-1):
            suffix[i] = suffix[i+1] + shifts[i]
        # return suffix
        for i in range (0,len(s)) :
            ans.append(
                chr((((ord(s[i])-ord("a"))+suffix[i])%26) + ord("a"))
            )
        return "".join(ans)

s =  "aaa"
shifts = [1,2,3]
sol = solution()
print(sol.shiftingLetters(s,shifts))  # Output: "rpl"  #