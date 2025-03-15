class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashS = {}
        freq = {}
        res = [""]*len(s)
        #used to store the index of each character in s also stored its freqency
        for index , i in enumerate(s):
                hashS[i] = index
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
        
        ordered_part = []
    #add the characters in s based on order order to the result
        for char in order:
            if char in freq:
                ordered_part.append(char * freq[char])  # Append multiple times
                del freq[char]  # Remove from dict

        unordered_part = []
    #add the characters in s that are not in order to the result
        for char in freq:
            unordered_part.append(char * freq[char])    
            

        res = "".join(ordered_part)
        res += "".join(unordered_part)
        return res


sol = Solution()    
order = "cba"
s = "abcdefef"
print(sol.customSortString(order,s))