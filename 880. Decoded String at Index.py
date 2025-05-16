class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0 
        for ch in s :
            if ch.isdigit():
                size*=int(ch)
            else:
                size +=1 
            
        for ch in reversed(s):
            
            k %= size 
            if ch.isdigit():
                size //= int(ch) 
            else : 
                size -=1 
                if k == 0 :
                    return ch 
        return ""
            
               
        
# Example usage:
s = Solution()
print(s.decodeAtIndex("a2b3c4d5e6f7g8h9", 10))  
print(s.decodeAtIndex("a2b3", 5))  # Output: "b"    
