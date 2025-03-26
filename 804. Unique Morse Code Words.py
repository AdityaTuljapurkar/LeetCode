from typing import List 
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--.."
}
        result = set()
        for word in words :
            morse = ""
            for char in word:
                morse += morseCode[char]
            result.add(morse)
        return len(result)
words = ["gin", "zen", "gig", "msg"]
s = Solution()
print(s.uniqueMorseRepresentations(words))
        