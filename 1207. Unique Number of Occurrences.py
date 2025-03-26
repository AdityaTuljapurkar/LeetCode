from typing import List 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}
        for i in arr:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

                
        comp_set = set()
        
        for key in hash_map:
            if hash_map[key] in comp_set:
                return False 
            else:
                comp_set.add(hash_map[key])
        return True
        

arr = [-3,0,1,-3,1,1,1,-3,10,0]
sol = Solution()
print(sol.uniqueOccurrences(arr))
        