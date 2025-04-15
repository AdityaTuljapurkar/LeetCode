from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_freq = sorted(freq.values(), reverse=True)
        
        pushes = 0
        for i, count in enumerate(sorted_freq):
            key_presses = (i // 8) + 1  # Each key can hold up to 9 letters
            pushes += key_presses * count
        
        return pushes
            
        
   
word = "aabbccddeeffgghhiiiiii"
print(Solution().minimumPushes(word))