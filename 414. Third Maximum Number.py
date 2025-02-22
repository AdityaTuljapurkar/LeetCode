from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        for num in nums :
            if num > max1 :
                max1, max2, max3 = num, max1, max2
            elif max1 > num > max2 :
                    max2 , max3 = num, max2
            else :
                if max2 > num > max3 :
                    max3 = num
        return max3 if max3 != float('-inf') else max1
print(Solution().thirdMax([1,2,-345678642])) # 1