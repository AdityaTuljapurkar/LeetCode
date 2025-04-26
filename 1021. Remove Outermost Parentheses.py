class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0
        for ch in s:
            if ch == '(':
                balance +=1
                if balance > 1:
                    result.append(ch)
            else:
                balance -=1 
                if balance > 0 :
                    result.append(ch)
        return ''.join(result)
# Test  
if __name__ == "__main__":
    s = "(()())(())"
    solution = Solution()
    print(solution.removeOuterParentheses(s))  # Output: "()()()"
    s = "(()())(())(()(()))"
    print(solution.removeOuterParentheses(s))  # Output: "()()()()(())"
    s = "()()"
    print(solution.removeOuterParentheses(s))  # Output: ""
                