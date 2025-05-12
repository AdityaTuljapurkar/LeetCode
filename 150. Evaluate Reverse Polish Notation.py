from typing import List 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #using stack 
        stack = []
        for ch in tokens:
            if ch in {"+", "-", "*", "/"}:
                num2 = int(stack.pop())
                num1 = int(stack.pop()) 
                orp = ch 
                match orp :
                    case "+":
                        res = num1 + num2 
                    case "-":
                        res = num1-num2 
                    case "*":
                        res = num1 * num2 
                    case "/":
                        res = num1/num2 

                stack.append(res)
            else : stack.append(int(ch))
        return stack[-1]



print(Solution().evalRPN(["4","13","5","/","+"])) 

            