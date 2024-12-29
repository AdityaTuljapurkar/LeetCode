s = "abc"
t = "ahbgdc"
class ABC : 
    def function(self,s,t):
        l = 0
        r = 0
        # if len(s)==0 : return True

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            
            r += 1
        return True if l == len(s) else False
                


obj = ABC()
print(obj.function(s,t))