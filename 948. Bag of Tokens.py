class Solution:
    def bagOfTokensScore(self, tokens, power: int) -> int:
        tokens.sort()
        score = 0
        i = 0
        j = len(tokens) -1
        maxScore = 0
        while i <= j:
            if power >= tokens[i]:
                score += 1
                power -= tokens[i]
                maxScore = max(maxScore, score)
                i+=1
                        
            elif score > 0  :
                power += tokens[j]
                j -= 1
                score -= 1
            else :break

        return maxScore
                

tokens = [100, 200, 300, 400]
power = 200
solution = Solution()
print(solution.bagOfTokensScore(tokens, power))  # Output: 2

    


