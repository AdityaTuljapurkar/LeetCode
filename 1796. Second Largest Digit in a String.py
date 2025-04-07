class Solution:
    def secondHighest(self, s: str) -> int:
        index = 1
        indexMap = set()
        arr = []
        for l in s :
            if ord(l) >= 48 and ord(l) <= 57:
                if int(l) not in indexMap:
                    arr.append(int(l))
                    indexMap.add(int(l))    
                else:
                    continue
        if len(arr) < 2:
            return -1
        arr.sort(reverse=True)
        return arr[1]
                

s ="ck077"
sol = Solution()
print(sol.secondHighest(s))