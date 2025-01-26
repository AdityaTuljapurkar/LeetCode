nums = [1,2,3]
k = 0
class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        s =0 
        e = 0 
        count [1,2,3] =0 
        res = 0 
        product = 1
        while e < len(nums):
            product *= nums[e]
            while product >= k and s <= e: 
                product //= nums[s]
                s +=1
            count = e - s + 1
            res += count
            e+=1

        return res
    
obj = Solution()
print(obj.numSubarrayProductLessThanK(nums, k))  # Output: 5