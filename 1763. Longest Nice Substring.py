class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        char_set = set(s)
        for i , ch in enumerate(s):
            if ch.swapcase() not in char_set:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return max(left, right, key=len)
        return s 
# Test
if __name__ == "__main__":
    s = "YazaAay"
    solution = Solution()
    print(solution.longestNiceSubstring(s))  # Output: "aAa" 