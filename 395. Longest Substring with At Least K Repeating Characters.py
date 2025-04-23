class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        freq = {}
        for ch in s :
            freq[ch] = freq.get(ch,0)+1
        count = 0 
        for ch in freq :
            
            if freq[ch] < k :
                sub = s.split(ch)
                result = []
                for i in sub :
                    result.append(self.longestSubstring(i,k))
                return max(result)if result else 0 
        return len(s)
    
# Test
if __name__ == "__main__":
    s = "aaabb"
    k = 3
    solution = Solution()
    print(solution.longestSubstring(s, k))  # Output: 3

    s = "ababbc"
    k = 2
    print(solution.longestSubstring(s, k))  # Output: 5

    s = "ab"
    k = 2
    print(solution.longestSubstring(s, k))  # Output: 0