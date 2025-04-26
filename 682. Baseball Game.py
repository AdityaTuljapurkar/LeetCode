from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch == '+':
                stack.append(stack[-1]+stack[-2])
            elif ch == 'D':
                stack.append(2*stack[-1])
            elif ch == 'C':
                stack.pop()
            else :
                stack.append(int(ch))
        return sum(stack)
# Test
if __name__ == "__main__":
    operations = ["5","2","C","D","+"]
    solution = Solution()
    print(solution.calPoints(operations))  # Output: 30
    operations = ["5","-2","4","C","D","9","+","+"]
    print(solution.calPoints(operations))  # Output: 27
    operations = ["1"]
    print(solution.calPoints(operations))  # Output: 1
    operations = ["1","C"]
    print(solution.calPoints(operations))  # Output: 0