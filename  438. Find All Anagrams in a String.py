s = "aaaaaaaaaa"
p = "aaaaaaaaaaaaa"
class Solution:
    def findAnagrams(self, s: str, p: str) :
        p_count = {}
        s_count = {}
        
        for r in range (len(s)) :
            s_count[s[r]] = s_count.get(s[r],0) +1
            p_count[p[r]] = p_count.get(p[r],0) +1
        
        count = [0] if s_count == p_count else []
        l= 0
    
            
        for r in range (len(p), len(s)) :
            s_count[s[r]] = s_count.get(s[r],0) +1
            s_count[s[l]] -= 1

            if s_count[s[l]] == 0 : 
                s_count.pop(s[l])
            
            l+=1

            if s_count == p_count : 
                count.append(l)

        return count
            


    
obj = Solution()
print(obj.findAnagrams(s, p))  # Output: {'a', 'b', '
        