s = "the sky is blue"
# Output: "blue is sky the"

def Function(Str:str):
    arr = Str.split()
    result = []
    i = len(arr)-1
    while i >= 0:
        result.append(arr[i])
        i -= 1
    return ' '.join(result)


print(Function(s))