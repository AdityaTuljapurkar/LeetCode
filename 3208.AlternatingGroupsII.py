colors =  colors = [0,1,0,0,1,0,1]
k = 6


class Solution:
    def numberOfAlternatingGroups(self, colors, k: int) -> int:
        N =len(colors)
        start = 0
        count  = 0
        for end in range (k-1,k-1+N) :
            if colors[start%N] == colors[end%N] and colors[start%N] != colors[(start+1)%N]:
                count += 1
            start += 1
            
        return count  
s = Solution()
print(s.numberOfAlternatingGroups(colors, k))  # Output: 3


