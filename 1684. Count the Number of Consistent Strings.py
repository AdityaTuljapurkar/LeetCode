from typing import List 
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = sorted(set(allowed))
        count = 0
        for word in words:
            wordSet = set(word)
            if wordSet.issubset(allowedSet):
                count += 1
        return count

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
s = Solution()
print(s.countConsistentStrings(allowed, words))