from typing import List 
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        
        count = [0]*n

        for i in range(len(requests)):
                for k in range(requests[i][0],requests[i][1]+1):
                    count[k] += 1

        hashCount = {}
        for index , i in enumerate(count):
            hashCount[index] = i
        hashCount = dict(sorted(hashCount.items(),key= lambda x:x[1],reverse=True))
        nums.sort(reverse=True)
        ans = [0]*n
        x =0
        for index in hashCount:
            ans[index] = nums[x]
            x += 1
        Sum = 0
        for i in range(len(requests)):
             for j in range(requests[i][0],requests[i][1]+1):
                 Sum += ans[j]
        
        return Sum%(10**9+7)
    

nums = [1,2,3,4,5,6]
requests = [[0,1]]
print(Solution().maxSumRangeQuery(nums, requests))