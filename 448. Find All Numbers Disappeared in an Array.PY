from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        n = max(max(nums),len(nums))
        result = []
        for i in range(1 , n+1):
            if i not in set_nums:
                result.append(i)
        return result
nums = [1,1]
sol = Solution()
print(sol.findDisappearedNumbers(nums))