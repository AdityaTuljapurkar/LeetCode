nums = [2,2,1,1,2,1,2]
k = 3
class Solution:
    def numberOfSubarrays(self, nums , k) :
        res ,l , mid ,odd= 0 , 0 ,0, 0
        for r in range(len(nums)) :
            if nums[r] % 2  :
                odd += 1
            
            while odd > k :
                if nums[l]%2:
                    odd -= 1
                l+=1
                mid = l
            
            if odd == k :
                while not nums[mid]%2 :
                    mid += 1
                res += (mid-l)+1

        return res
obj = Solution()    
print(obj.numberOfSubarrays(nums , k))  # 8


    
    

        
    