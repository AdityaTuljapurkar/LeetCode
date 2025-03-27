class Solution:
    def countLargestGroup(self, n: int) -> int: 
        freq = {}
        for i in range(1, n + 1):
            
            sum_digits = sum(int(d) for d in str(i))
            if sum_digits in freq:
                freq[sum_digits] += 1
            else:
                freq[sum_digits] = 1
        max_count = 0
        max_value = max(freq.values())
        # return max_value
        for key , value in freq.items():
            if value == max_value:
                max_count += 1
        return max_count 
    


n= 13 
s = Solution()
print(s.countLargestGroup(n))
