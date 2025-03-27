class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        freq = {}
        for  letter in s:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        for letter in t:
            if letter in freq:
                freq[letter] -= 1
                if freq[letter] == 0:
                    del freq[letter]
            else:
                return False 
        return len(freq) == 0
# Test cases
s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: True