class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people .sort()
        l =0 
        r = len(people)-1
        count = 0
        while l<=r:
            if people[l]+people[r] <= limit :
                l += 1
                r -= 1
                count += 1
            else: 
                if people[r] <= limit:
                    r -= 1
                    count += 1
                else:
                    r -= 1
        return count
    

        

print(Solution().numRescueBoats([1,2],3) )
print(Solution().numRescueBoats([3,2,2,1],3) )
            
