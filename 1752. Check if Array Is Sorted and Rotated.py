from typing import List
class solution :
    def checkArraySorted (self,nums : List[int])-> bool :
        length = 0
        maxLen = 0 
        N = len(nums)
        start = 0 

        for end in range (2*N-1) :
            if nums[end%N] <= nums[(end+1)%N] :
                maxLen = max (maxLen , end - start + 1)
                if maxLen == N :
                    return True
            else : 
                start = end
                
        return False 
nums = [3,4,5,1,2]
sol = solution ()
print (sol.checkArraySorted(nums))
            
