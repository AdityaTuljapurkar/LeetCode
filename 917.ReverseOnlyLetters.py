class Solution :

    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1

        while l < r:

            if ((65 <= ord(s[l]) <= 90) or (97 <= ord(s[l]) <= 122)) and ((65 <= ord(s[r]) <= 90) or (97 <= ord(s[r]) <= 122)):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

            elif not ((65 <= ord(s[l]) <= 90) or (97 <= ord(s[l]) <= 122)):
                l += 1

            elif not ((65 <= ord(s[r]) <= 90) or (97 <= ord(s[r]) <= 122)):
                r -= 1

        return "".join(s)
    
    
s = "a-bC-dEf-ghIj"
sol = Solution ()
print(sol.reverseOnlyLetters(s))

        

