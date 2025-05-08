class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0 
        max_open = 0
        for ch in s :
            if ch  == "(":
                min_open += 1 
                max_open +=1
            elif ch == ")":
                min_open = max(min_open - 1, 0)
                max_open -= 1
            else :
                max_open +=1
                min_open = max(min_open-1, 0)
            if max_open <= 0 : 
                return False

        return min_open == 0  

#test 
sol = Solution()
print(sol.checkValidString("(*)*)"))