#Finding the best stock exchange

def maxprofit(prices):
    max_profit = 0 
    l,r = 0 ,1
    while r<len(prices) :
        if prices[l]<prices[r] :
            profit = prices[r]-prices[l]
            max_profit = max(max_profit,profit)

        else : l =r
        r+=1
    return  max_profit
    


print(maxprofit([7,1,5,3,6,4]))  