class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if lengths are equal
        if len(word1) != len(word2):
            return False

        # Frequency dictionaries
        freq1 = {}
        freq2 = {}

        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1

        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1

        # Condition 1: Same set of characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Condition 2: Same multiset of frequencies
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if lengths are equal
        if len(word1) != len(word2):
            return False

        # Frequency dictionaries
        freq1 = {}
        freq2 = {}

        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1

        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1

        # Condition 1: Same set of characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Condition 2: Same multiset of frequencies
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True
