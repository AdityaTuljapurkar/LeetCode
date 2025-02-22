class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        res1 = False
        res2 = False
        for i in range(len(s1)):
            if s1[i] >= s2[i]:
                res1 = True
            else:
                res1 = False
                break
        for i in range(len(s2)):
            if s2[i] >= s1[i]:
                res2 = True
            else:
                res2 = False
                break
        return res1 or res2
s1 = "szy"
s2 = "cid"
sol = Solution()
print(sol.checkIfCanBreak(s1, s2))
                