from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            maxNum = num 
            for i in range(nums2.index(num)+1,len(nums2)):
                if nums2[i] > maxNum:
                    maxNum = nums2[i]
                    break
            res.append(maxNum) if maxNum > num else res.append(-1)
        return res
    
# Test
if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    solution = Solution()
    print(solution.nextGreaterElement(nums1, nums2))  # Output: [-1,3,-1]
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    print(solution.nextGreaterElement(nums1, nums2))  # Output: [3,-1]
    nums1 = [1,2,3]
    nums2 = [3,2,1]
    print(solution.nextGreaterElement(nums1, nums2))  # Output: [-1,-1,-1]