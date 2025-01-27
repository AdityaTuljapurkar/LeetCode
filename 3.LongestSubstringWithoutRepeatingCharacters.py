class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        max_length = 0
        start = 0
        for end in range(len(s)):
            if s[end] not in hash_map:
                hash_map[s[end]] = 0
            hash_map[s[end]] += 1
            while hash_map[s[end]] > 1:
                hash_map[s[start]] -= 1
                start+=1
            max_length = max(max_length,end-start+1)
        return max_length

sol = Solution()
print(sol.lengthOfLongestSubstring("bbbbbb")) # 3