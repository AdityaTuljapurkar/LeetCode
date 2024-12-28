s = "leetcode"
# Output: "leotcede"


def Solution(Str):
    Vowel = {"a","e","i","o","u","A","E","I","O","U"}
    Str = list(Str)
    i =0 
    j = len(Str)-1
    while i<j:
        if Str[i] in Vowel and Str[j] in Vowel:
            Str[i],Str[j]=Str[j],Str[i]
            i +=1
            j-=1
        elif Str[i] in Vowel and Str[j] not in Vowel:
            j-=1
        elif Str[i] not in Vowel and Str[j] in Vowel:
            i +=1
        else : 
            i +=1
            j-=1
    
    return "".join(Str)




print(Solution(s))