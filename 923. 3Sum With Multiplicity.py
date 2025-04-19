from typing import List     
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int: 
        freq= {}
        for num in arr :
            freq[num] = freq.get(num,0)+1
        keys = sorted(freq.keys())
        output  = 0 
        for  l , x in enumerate(keys):
            for r , y in enumerate(keys):
                if x >y : 
                    continue
                z = target - x - y
                if z < y :
                    continue
                if z in freq:
                    if x == y == z :
                        output += freq[x] * (freq[x]-1) * (freq[x]-2) // 6
                    elif x == y != z :
                        output += freq[x] * (freq[x]-1) // 2 * freq[z]
                    elif x != y == z :
                        output += freq[y] * (freq[y]-1) // 2 * freq[x]
                    elif x != y != z :
                        output += freq[x] * freq[y] * freq[z]
        return output % (10**9 + 7)
# Test
if __name__ == "__main__":
    arr = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    solution = Solution()
    print(solution.threeSumMulti(arr, target))  # Output: 10