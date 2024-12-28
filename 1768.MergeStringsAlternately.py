word1 = "abc"
word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c 

def mergeAlternately(word1, word2):
    result = []
    i = 0 
    j = 0 
    
    while i <len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i +=1
        j+=1

    while i <len(word1):
        result.append(word1[i])
        i+=1
    while j < len(word2):
        result.append(word2[j])
        j+=1
    return "".join(result)

print(mergeAlternately(word1,word2))