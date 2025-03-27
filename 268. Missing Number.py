from typing import List 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n + 1):
            res += (i - nums[i] if i < n else i)
        return res
# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 0, 1]
    print(solution.missingNumber(nums))  # Output: 2
    nums = [0, 1]