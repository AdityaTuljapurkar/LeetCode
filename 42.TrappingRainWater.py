from typing import List 
class Solution :
    def trap (self,height :List[int])-> int :
        
        if not height : return 0

        l,r = 0 , len(height)-1
        maxLeft = height[l]
        maxRight = height[r]
        res = 0


        while l < r :
            if maxLeft < maxRight :
                l+=1 
                maxLeft = max(maxLeft,height[l])
                res += maxLeft - height[l]

            else :
                r-=1
                maxRight = max(maxRight , height[r])
                res+= maxRight - height[r]
        
        return res 
    
# height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution ()
print(sol.trap(height))