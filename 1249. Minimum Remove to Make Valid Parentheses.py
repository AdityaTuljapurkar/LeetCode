class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        balance = 0
        s = list(s)
        i = 0
        while i < len(s):
            if s[i] == '(':
                balance += 1
            elif s[i] == ')':
                if balance == 0:
                    s.pop(i)
                    i -= 1
                else:
                    balance -= 1
            i += 1

        if balance < 0:
            z = 0
            while z < len(s) and balance < 0:
                if s[z] == ')':
                    s.pop(z)
                    balance += 1
    
                else:
                    z += 1
        
        if balance > 0:
            j = len(s) - 1
            while balance > 0 and j >= 0:
                if s[j] == '(':
                    s.pop(j)
                    balance -= 1
                j -= 1
            
        return ''.join(s) 

# Test
if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    solution = Solution()
    print(solution.minRemoveToMakeValid(s))  # Output: "lee(t(c)o)de"
    s = "a)b(c)d"
    print(solution.minRemoveToMakeValid(s))  # Output: "ab(c)d"
    s = "))(("
    print(solution.minRemoveToMakeValid(s))  # Output: ""
    s = "(a(b(c)d)"
    print(solution.minRemoveToMakeValid(s))  # Output: "a(b(c)d)"
