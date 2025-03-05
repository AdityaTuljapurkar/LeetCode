from typing import List

class Solution:
    def function(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for s in strs:
            key = tuple(sorted(s))
            
            if key not in hashmap:
                hashmap[key] = []
                
            hashmap[key].append(s)
        
        return list(hashmap.values()) 

# Test case
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().function(strs))

