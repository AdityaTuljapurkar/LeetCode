str1 = "ABCABCABC"
str2 = "ABCABC"
# Output: "ABC"
def GCD(A,B):
    if B == 0:
        return A
    else :
        return GCD(B, A % B)

def common_string(str1, str2):
    L1 = len(str1)
    L2 = len(str2)
    

    
    if L1 > L2:
        gcd = GCD(L1,L2)
    else : 
        gcd = GCD(L2,L1)

    return str2[0:gcd]

print(common_string(str1,str2))






