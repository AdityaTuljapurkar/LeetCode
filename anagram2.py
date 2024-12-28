from collections import Counter
A = "cbaebabacd"
B = "abc"


def anagram(A,B):
    windowB = Counter(B)
    
    l= 0
    r = len(B)
    res = []
    while r < len(A) :
        windowA = Counter(A[l:r])
        if windowA == windowB:
            res.append(l)
        l+=1   
        r+=1
        
    return res 

print(anagram(A,B))






    