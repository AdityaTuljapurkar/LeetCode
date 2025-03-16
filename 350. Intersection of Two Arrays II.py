from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        res = []
        for i in nums1:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for num in nums2:
            if num in freq and freq[num]> 0:
                res.append(num)
                freq[num] -= 1
        return res
sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersect(nums1,nums2)) # [2,2]