from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num,0)+1
        freq = dict(sorted(freq.items(),key = lambda x : x[1],reverse=  True))
        res= 0 
        length = 0 
        maxLen = len(arr)//2
        for key in freq:
            length += freq[key]
            res +=1
            if length >= maxLen :
                break 
        return res  
# Example usage 
arr = [3,3,3,3,5,5,5,2,2,7]
print(Solution().minSetSize(arr))