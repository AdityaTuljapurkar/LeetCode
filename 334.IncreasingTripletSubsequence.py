nums = [2,1,5,0,4,6]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
class abcd :
    def slidingwindow(nums):
        n = len(nums)
        k = 2
        result = True
        while k<n: # k is the size of the window
            i=k-2
            j=k-1
            if nums[i] <= nums[j] and nums[j] <= nums[k] :
                i+=1
                j+=1
                k+=1
            else :
                result = False
                break
        return result
    print(slidingwindow(nums)) # True