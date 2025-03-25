from typing import List 
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashMap = {}
        for i in range(len(names)):
            hashMap[heights[i]] = names[i]
        hashMap =  dict(sorted(hashMap.items(),key=lambda x : x[0], reverse=True))
        res = []
        res = list(hashMap.values())
                        
        
        return res
           
names = ["Alex", "Ben", "Charlie", "David"]
heights = [5, 3, 2, 6]
s = Solution()
print(s.sortPeople(names, heights))