target = 11
nums = [1,1,1,1,1,1,1,1]
import math
import math
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = total = 0
        min_len = math.inf

        for end in range(len(nums)):
            total += nums[end]
            
            while total >= target:
                min_len = min(min_len, end - start + 1)
                total -= nums[start]
                start += 1

        return 0 if min_len == math.inf else min_len


solution = Solution()
print(solution.minSubArrayLen(target,nums))
                
