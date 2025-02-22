# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         text = text.lower()
#         textarr = text.split() 
#         hashArr = {}

#         for i in range(len(textarr)):
#             hashArr[textarr[i]] = len(textarr[i])
        
#         hashArr = sorted(hashArr.items(),key = lambda x : x[1])
#         for i in range(len(hashArr)):
#             textarr[i] = hashArr[i][0]
#         textarr[0]= textarr[0].capitalize()
#         return " ".join(textarr)

class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        textarr = text.split()
        textarr = sorted(textarr, key = len)
        textarr[0] = textarr[0].capitalize()
        return " ".join(textarr)
        
        

text = "Leetcode is cool"   
sol = Solution()
print(sol.arrangeWords(text))