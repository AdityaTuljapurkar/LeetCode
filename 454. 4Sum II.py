from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq = {}
        res : int =0
        #creating an n^2 loop 
        for num1 in nums1 :
            for num2 in nums2 :
                Sum = (num1+num2)
                freq[Sum] =freq.get(Sum,0)+1
        for num3 in nums3 :
            for num4 in nums4:
                Target = num3+num4
                if (Target*-1) in freq :
                    res+= freq[Target*-1]
        return res



nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]        
print(Solution().fourSumCount(nums1,nums2,nums3,nums4))