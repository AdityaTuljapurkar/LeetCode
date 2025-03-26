from typing import List 
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_map = {}
        for i in arr:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        # print (hash_map)

        count = 0
        for i in arr : 
            if hash_map[i]==1 :
                count += 1
                if count == k:
                    return i
        return ""


arr = ["a", "b", "c", "a", "b", "c", "a", "b", "c"]
k = 2
# arr = ["aaa","aa","a"]
# k = 1

sol = Solution()
print(sol.kthDistinct(arr, k))
        