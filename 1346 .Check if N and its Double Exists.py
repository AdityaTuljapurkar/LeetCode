from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashset = set(arr)
        for i in range(len(arr)):
            if arr[i] * 2 in hashset and i!= arr.index(arr[i] * 2) :
                return True
        return False
# Test the function
sol = Solution()
arr = [2, 2, 5, 3]
result = sol.checkIfExist(arr)
print(result)  # Output: True