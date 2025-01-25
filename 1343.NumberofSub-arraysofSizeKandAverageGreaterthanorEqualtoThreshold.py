arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

class ABC :
    def function (self,arr,k,treshold):
        start,end,count,sum = 0,0,0,0

        #calculating for end ==2
        for end in range(k):
            sum += arr[end]
        
        if sum/k >= treshold : 
            count+=1

        for end in range(k,len(arr)):
            sum += arr[end]
            sum-= arr[start]
            start+=1
            
            if sum/(k) >= treshold :
                count+=1
        return count

obj = ABC()
print(obj.function(arr,k,threshold))