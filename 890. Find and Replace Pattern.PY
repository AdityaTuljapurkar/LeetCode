from typing import List 
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def convert(word:str)-> List[int]:
            hashMap =  {}
            res = []
            for i , ch in enumerate(word):
                if ch not in hashMap:
                    hashMap[ch] = i
                res.append(hashMap[ch]) 
            return res

        pattern = convert(pattern)
        result = []
        for i in range(len(words)):
            word_pattern = convert(words[i])
            if word_pattern == pattern:
                result.append(words[i])
        return result

# Example usage
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print(Solution().findAndReplacePattern(words, pattern))

                