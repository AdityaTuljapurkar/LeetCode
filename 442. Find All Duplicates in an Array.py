from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        num_dict = set()
        for num in nums:
            if num not in num_dict:
                num_dict.add(num)
            else:
                res.append(num)
        return res
# Example usage
nums = [4,3,2,7,8,2,3,1]
print(Solution().findDuplicates(nums))
# Output: [2, 3]