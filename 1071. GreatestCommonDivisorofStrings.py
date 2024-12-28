
from collections import Counter 
str1 = "ABCABC"
str2 = "ABC"
# Output: "AB"
sett = {}
for i in str2 :
    sett[i] = 0

# for i in str1:
#     if str1[i] in sett:
#         sett[i]+=1
x = [   ]

for w in sett.keys():
   x.append(w)
    
print(x)

