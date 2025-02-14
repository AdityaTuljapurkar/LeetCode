from typing import List
class Solution:
    def sortSentence(self, s: str) -> str:
        arr =s.split()
        res:List[str] = [""]*len(arr)

        for words in arr : 
            pos = int(words[-1])-1 
            x = words[:-1]
            res[pos] = x 
        
        return " ".join(res)
    




s = "is2 sentence4 This1 a3"   
sol = Solution()
print(sol.sortSentence(s))