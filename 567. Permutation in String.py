s1 = "ab"
s2 = "eidboaoo"

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1set = {}
        S2set = {}
        if len(s1)> len(s2) :
            return False
        for i in range(len(s1)):
            S1set[s1[i]] = S1set.get(s1[i], 0)+1
            S2set[s2[i]] = S2set.get(s2[i], 0)+1
        
        val = True if S1set == S2set else False
        start = 0
        for end in range(len(s1),len(s2)):
            S2set[s2[end]] = S2set.get(s2[end], 0)+1
            S2set[s2[start]] -=1
            
            if S2set[s2[start]] == 0 :
                S2set.pop(s2[start])
            start+=1

            if S2set == S1set :
                return True
        
        return val
        
            

solution = Solution()
print(solution.checkInclusion(s1,s2))  # True