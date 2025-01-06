s = "aongeono"
k = 3
class ABC:
    def function(self, s, k):
        vowels = {"a","e","i","o","u"}
        count ,l ,res = 0 , 0, 0
        #using sliding window of size k 
        for  r in range(0,len(s)):
            count+=1 if s[r] in vowels else 0 
            if (r-l)+1 > k:
                count -=1 if s[l] in vowels else 0 
                l+=1
            res = max(count,res)
        return res 
    

obj = ABC()
print(obj.function(s,k))  # Output: 3