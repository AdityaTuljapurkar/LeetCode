class Solution:
    def fib(self, n: int) -> int: 
        #base case :
        if n == 0:
            return 0 
        if n == 1:
            return 1
        #recursive case :
        return self.fib(n-1) + self.fib(n-2)
# Test cases
n = 10
print(Solution().fib(n)) # 1
n = 3   
print(Solution().fib(n)) # 2