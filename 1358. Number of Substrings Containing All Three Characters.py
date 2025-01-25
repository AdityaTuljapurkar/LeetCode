s = "abcabc"
class ABC :
    def function(self,s):
        start,count = 0 , 0
        lastSeen = {"a":-1,"b":-1,"c":-1}
        
        for end in range(len(s)):
            lastSeen[s[end]] = end
            
            if lastSeen["a"] > -1 and lastSeen["b"] > -1 and lastSeen["c"] > -1 :
                
                start = min(lastSeen.values())
                count += 1+start

        return count
        # return lastSeen.get(min(lastSeen))
obj = ABC()
print(obj.function(s)) 

