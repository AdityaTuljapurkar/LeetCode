from typing import List 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        #using two pointer approach
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else: 
                nums1[last]= nums2[n-1]
                n-=1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
        return nums1


print(Solution().merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,3], n = 3)) #[0, 1, 2, 2, 3, 5, 6]