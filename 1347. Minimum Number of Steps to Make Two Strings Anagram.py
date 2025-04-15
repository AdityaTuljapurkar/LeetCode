class Solution:
    def minSteps(self, s: str, t: str) -> int:
    #    if string is given use frequency array 
        # frequency array
        freq_s = [0] * 26
        freq_t = [0] * 26

        # # count frequency of each character in s
        for i in range(len(s)):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_t[ord(t[i]) - ord('a')] += 1
        # count number of steps to make anagram
        steps = 0 
        for i in range(26):
            steps += abs(freq_s[i] - freq_t[i])
        return steps // 2



s = "leetcode"
t = "practice"
print(Solution().minSteps(s, t))