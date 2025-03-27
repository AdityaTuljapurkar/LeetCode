class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for letter in range( len(s)) :
            if s[letter] in freq:
                freq[s[letter]] += 1
            else:
                freq[s[letter]] = 1
        
        
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
s = "leetcode"
sol = Solution()
print(sol.firstUniqChar(s))