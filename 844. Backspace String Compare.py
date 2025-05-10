class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stac_s = []
        stac_t = []
        for ch in s:
            if not stac_s and ch == "#": continue
            if stac_s and ch == "#":
                stac_s.pop()
            else : 
                stac_s.append(ch)

        for ch in t :
            if not stac_t and ch == "#": continue 
            if stac_t and ch == "#":
                stac_t.pop()
            else : 
                stac_t.append(ch)

        return stac_t == stac_s 
    
s = "y#fo##f"
t = "y#f#o##f"
print(Solution().backspaceCompare(s,t))
              