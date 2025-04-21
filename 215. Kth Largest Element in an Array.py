import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-num for num in nums]
        heapq.heapify(maxheap)
        for _ in range(k):
            kth_largest = heapq.heappop(maxheap)
        return -kth_largest
# Test
if __name__ == "__main__":
    nums = [-987,-8,99]
    k = 2
    solution = Solution()
    print(solution.findKthLargest(nums, k))  # Output: 5