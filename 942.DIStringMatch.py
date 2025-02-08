from typing import List
class Solution :
    def DIStringMatch(self,s:str)->List[int] :
        l,r = 0 , len(s) 
        nums:List = []
        i=0 
        while l<r :
            if s[i] == "I" :
                nums.append(l)
                l+=1
            if s[i] == "D" :
                nums.append(r)
                r-=1
            i+=1 

        nums.append(l)
        return nums

s = "DDI" 
sol = Solution()
print(sol.DIStringMatch(s))