nums = [5,2,1,2,5,2,1,2,5]
class ABC :
    def function(Self,nums):
        optimal_Sub_array , start , Sum =0,0,0
        countMap = {}

        for num in nums :
            countMap[num]=  0
        
        for end in range(len(nums)) :

            countMap[nums[end]] += 1
            Sum += nums[end]

            while countMap[nums[end]] > 1 :
                    countMap[nums[start]] -= 1
                    Sum -= nums[start]
                    start +=1

            optimal_Sub_array = max(optimal_Sub_array,Sum)
            
        return optimal_Sub_array 
    
obj = ABC()
print(obj.function(nums))