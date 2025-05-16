from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0 
        r = n-1 
        #removing the postfix
        # calculating the prefix  
        while l < n-1 and arr[l] <= arr[l+1]:
            l +=1 

        # if the array is already sorted
        if l == n-1:
            return 0
        # remov ing the prefix
        # calculating the postfix
        while r > 0 and arr[r] >= arr[r-1]:
            r-=1 

#findning minimum elimination 
        res = min(r , n-1-l ) 
        #finding the middle element  
        i,j = 0,r 
        while i <=l and j <n:
            if arr[i]<=arr[j]:
                res = min(res,j-i-1)
                i+=1 
            else:
                j+=1
        return res
# Test cases
print(Solution().findLengthOfShortestSubarray([1,2,3,10,4,2,3,5])) # Expected output: 3x