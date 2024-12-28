candies = [2,3,5,1,3]
extraCandies = 3
# Output: [true,true,true,false,true] 
def kidsWithCandies(candies, extraCandies):
    max_candy = max(candies)
    result = []
    for candy in candies:
        if candy + extraCandies < max_candy : 
            result.append(False)
        else : result.append(True)
    return result




print(kidsWithCandies(candies, extraCandies))