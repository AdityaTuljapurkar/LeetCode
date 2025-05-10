from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []  # Initialize empty stack
        n = len(nums)
        
        for i, num in enumerate(nums):
            # Calculate how many elements remain after current position
            remaining = n - i - 1
            
            # Pop from stack only if:
            # 1. Stack is not empty
            # 2. Current number is smaller than stack top (more competitive)
            # 3. We still have enough remaining elements to fill the stack to size k
            while stack and stack[-1] > num and len(stack) + remaining >= k:
                stack.pop()
                
            # Add current number if stack hasn't reached size k
            if len(stack) < k:
                stack.append(num)
                
        return stack
    
#test 
nums= [2,4,3,3,5,4,9,6]
k =4
print(Solution().mostCompetitive(nums,k))