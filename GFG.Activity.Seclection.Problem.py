from typing import List, Tuple
def Function ( start:List[int] , end:List[int]) -> int:

    activites = zip(start,end)
    activites = sorted(activites,key=lambda x: x[1]) 
    count = 0 
    count = 1  # First activity is always selected
    last_end = activites[0][1]  # End time of first activity
    
    for i in range(1, len(activites)):
        if activites[i][0] >= last_end:  # If current start time >= last end time
            count += 1
            last_end = activites[i][1]
    return count

    # for s, f in activites:
    #     print (s,f)
    # return activites


start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
print(Function(start,end))