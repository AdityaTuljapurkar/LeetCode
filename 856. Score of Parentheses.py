class Solution:
    def scoreOfParentheses(self,s: str) -> int:
        stack =  []
        for ch  in s :
            if ch == "(":
                stack.append(-1)
            else :
                if stack[-1]==-1 :
                    stack.pop()
                    stack.append(1)
                else :
                    temp = 0 
                    while stack and stack[-1] != -1 :
                        temp += stack.pop()
                    stack.pop()
                    stack.append(2*temp)
        return sum(stack)
# Test
if __name__ == "__main__":
    s = "(()(()))"
    solution = Solution()
    print(solution.scoreOfParentheses(s))  # Output: 6
    s = "()"
    print(solution.scoreOfParentheses(s))  # Output: 1
    s = "(())"
    print(solution.scoreOfParentheses(s))  # Output: 2
    s = "(()())"
    print(solution.scoreOfParentheses(s))  # Output: 4