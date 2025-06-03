from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums  :
            hashMap[i] = 1+ hashMap.get(i,0)
        

        hashMap = dict(sorted(hashMap.items(),key = lambda x : x[1],reverse= True))
        res = []
        count = 0
        for i in hashMap : 
            res.append(i)
            count +=1
            if count == k :
                break
            



        return res

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))