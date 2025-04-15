class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for i in word :
            freq[i] = freq.get(i, 0) + 1
        freq = dict(sorted(freq.items(),key= lambda x : x[1], reverse = True))
        

        output  =0
        for count,i in enumerate(freq.keys()):
            output += ((count//8)+1 )* freq[i]
        return output
    
            
        
   
word = "aabbccddeeffgghhiiiiii"
print(Solution().minimumPushes(word))