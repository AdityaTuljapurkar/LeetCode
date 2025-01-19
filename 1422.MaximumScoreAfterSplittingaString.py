s = "1111"
class ABC :
    def function(self,s):
        noOf1s = 0
        for nums in s : 
            if nums == '1' :
                noOf1s +=1
        noOf0s = 0
        start = 0
        maxVal = 0
        while start < len(s)-1 :
            if s[start] == '0' :
                noOf0s += 1
            else : noOf1s -=1
            maxVal = max(maxVal,noOf1s+noOf0s)
            start += 1
        return maxVal
obj = ABC()
print(obj.function(s))

