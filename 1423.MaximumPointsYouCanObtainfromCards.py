class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        l =  0 
        r =  len(cardPoints)- k
        total = sum (cardPoints[r:])
        maxPoints = total
        while r <len(cardPoints):
            total += cardPoints[l] -cardPoints[r]
            maxPoints = max(maxPoints,total)
            l += 1
            r += 1
        return maxPoints
    
obj = Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(obj.maxScore(cardPoints,k))