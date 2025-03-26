from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        freq = {}
        for num in arr1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        result = []
        for num in arr2:
            result.extend([num]*freq[num])
            del freq[num]
        
        for num in sorted(freq.keys()):
            result.extend([num]*freq[num])
        
        return  result

# Time complexity: O(n)
# Space complexity: O(n)
# Runtime: 40 ms, faster than 94.09% of Python3 online submissions for Relative Sort Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Relative
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
sol = Solution()
print(sol.relativeSortArray(arr1, arr2)) # [[22, 22], [28, 28], [8, 8], [6, 6]]
        
        