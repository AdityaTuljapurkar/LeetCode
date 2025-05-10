class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s :
            if stack : 
                if stack[-1] == "{":
                    opposite = "}"
                elif stack[-1] == "[":
                    opposite = "]"
                elif stack[-1] == "(":
                    opposite = ")"
                else : opposite = -1
                if ch is opposite : 
                    stack.pop()
                    continue
            stack.append(ch)
        return True if len(stack)== 0 else False

# test
s = "}["

print(Solution().isValid(s))