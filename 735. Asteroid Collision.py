from typing import List 
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def calStrike(curr , top ):
            if top > 0 and curr < 0 :
                if top > abs(curr) : #top left after collide 
                    return top 
                elif top == abs(curr ): #both distroyed 
                    return None 
                else :
                    return curr #current left after collide 
            elif top < 0 and curr > 0 : #no collsion 
                return curr 
            else :
                return curr 
        for curr in asteroids:
            while stack and curr < 0 and stack[-1] > 0:
                top = stack[-1]
                val = calStrike(curr, top)

                if val == curr:
                    stack.pop()  # top is destroyed, curr survives, check again
                elif val is None:
                    stack.pop()  # both destroyed
                    curr = None
                    break
                else:  # curr destroyed
                    curr = None
                    break

            if curr is not None:
                stack.append(curr)

        return stack
    
sol = Solution()
print(sol.asteroidCollision([10, 2, -5]))  # Output: [10]
print(sol.asteroidCollision([8, -8]))      # Output: []
print(sol.asteroidCollision([-2, -1, 1, 2]))# Output: [-2, -1, 1, 2]





