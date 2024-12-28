flowerbed = [1,0,0,0,1]
n = 2
# flowerbed = [1,0,0,0,1]
# n = 1
# flowerbed = [0, 0, 1, 0, 0] 
# n = 2

def placeFlower(flowerbed , n):
    if n == 0:
        return True
    i =0 
    while i < len(flowerbed):
        if i<len(flowerbed)-2 and flowerbed[i] == 0 and i> 0 and flowerbed[i-1] == 0  and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1  
            i+=1
        elif flowerbed [i] == 0 and i == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n-=1 
            i+=1
        elif flowerbed [i] == 0 and i == len(flowerbed)-1 and flowerbed[i-1]==0 : 
            n -=1
            flowerbed[i] = 1
            i+=1
        else : i +=1

    if n == 0:
        return True
    else : 
        return False
        
print(placeFlower(flowerbed,n))
        



