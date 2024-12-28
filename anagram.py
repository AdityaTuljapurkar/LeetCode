A = "cbaebabacd"
B = "abc"
# [0, 6]

# map = {}
# for n,i in enumerate(B):
#    map[n]= i


def anagram(A,B):

    sett = set()
    def addSet():
        for x  in  range(len(B)):
            sett.add(B[x])
    res= []
    l = 0
    r  = 1 
    # addSet()
    while r <len(A):
        if A[r] in sett:
            sett.remove(A[r])
        
        if not sett :
            res.append(l)
            addSet()
        if sett :
            addSet()
        l +=1
        r+=1

    return res 


print(anagram(A,B))  # [0, 6]  



# https://chatgpt.com/share/672a97ab-95a8-8005-8c68-e401ccaa2f31