# chars = ["a","a","b","c","c","c"]
# chars = ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

class XYZ :
    def compress(self,chars):
        if len(chars) == 0:
            return 0
        if len(chars) == 1:
            return chars[0]
        charmap = {}
        for i in chars :
            charmap[i]= 0
        for  i in chars :
            if i in charmap:
                charmap[i]+=1
        result = []
        for key in charmap :
            result.append(key)
            if charmap[key] > 1:
                for digit in str(charmap[key]):
                    result.append(digit)
        

        return result
    

obj1 = XYZ()
print(obj1.compress(chars)) 
