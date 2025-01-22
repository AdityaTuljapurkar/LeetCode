
colors = [0,1,0,0,1]
class ABC : 
    def function(self,colors):
        count = 0 
        k = len(colors)
        
        for i in range(1,len(colors)+1):
            if  colors[(i-1)%k] != colors[i%k]  and colors[(i-1)%k] == colors[(i+1)%k]: 
                count+=1
        return count
                

obj = ABC()
print(obj.function(colors))  
