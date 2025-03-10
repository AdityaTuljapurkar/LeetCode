s = "krrgw"
t = "zjxss"
maxCost = 19

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        max_len = 0
        cost = 0
        
        for end in range(len(s)):
            cost += abs(ord(s[end])-ord(t[end]))
            
            while cost > maxCost:
                cost -= abs(ord(s[start])-ord(t[start]))
                start += 1
            
            max_len = max(max_len,end-start +1)
        return max_len
    

obj = Solution()
print(obj.equalSubstring(s, t, maxCost))  # Output: 2

