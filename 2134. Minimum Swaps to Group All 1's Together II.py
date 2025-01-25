class Solution:
    def minSwaps(self, nums) -> int:
        N = len(nums)
        Sum1s = nums.count(1)
        start = 0 
        count  = maxCount = 0
        for r in range(N*2) :
            if nums[r%N]:
                count +=1
            if r- start+1 > Sum1s :
                count -= nums[start%N]
                start +=1
            maxCount = max(maxCount , count)
            
        return Sum1s-maxCount 
obj = Solution()
print(obj.minSwaps([1,1,0,0,1])) # 1
        