height = [1,3,5,7,9]
# Output: 49
import math
class ABC :
    def function(self,height):
        l =0 
        r=len(height)-1
        max_area = -(math.inf)
        while l<r:
            area = min(height[l],height[r])*(r-l)
            max_area = max(max_area,area)
            if height[l]<height[r]:
                l+=1
            else :
                r-=1
        return max_area
obj = ABC()
print(obj.function(height))
