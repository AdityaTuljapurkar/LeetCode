from typing import List, Tuple
class solution :
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxascend = 1
        maxdescend = 1
        ascend = 1
        descend = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                ascend += 1
                descend = 1
            elif nums[i] < nums[i-1]:
                descend += 1
                ascend = 1
            else:
                ascend = 1
                descend = 1

            maxascend = max(maxascend, ascend)
            maxdescend = max(maxdescend, descend)

        return max(maxascend, maxdescend)


