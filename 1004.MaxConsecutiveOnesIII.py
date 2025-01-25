nums = [1,1,1,0,0,0,1,1,1,1,0] 
k = 2
class Solution:
    def longestOnes(self, nums, k) :
        start = maxCount =0

        for end in range(len(nums)) :
            if not nums[end] :
                k -=1

            while k < 0 :
                if not nums[start] :
                    k += 1
                start += 1
            maxCount = max(maxCount, end - start + 1)

        return maxCount

obj = Solution()
print(obj.longestOnes(nums, k))  # Output: 6
        