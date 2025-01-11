# minimum magnetic force between any two balls is maximum.
class ABC  :
    def function (self , position,m):
        position.sort()
        def ballposition(min_force):
            count = 1
            last_pos = position[0]
            for  i in range(1,len(position)):
                force = position[i]- last_pos
                if force >= min_force:
                    count += 1
                    last_pos = position[i]
                if count == m : return True 
            return False
        
        result = 0  
        low = 1
        high = position[-1] - position[0]
        while low <= high:
            mid = (high+low)//2
            if ballposition(mid):
                result = mid
                low  = mid+1
            else:
                high = mid-1
        return result
    

obj = ABC()
position = [1, 2, 8, 4, 9]
m = 3
print(obj.function(position, m))  # Output: 3



