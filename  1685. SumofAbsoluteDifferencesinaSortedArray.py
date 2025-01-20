# nums = [1,4,6,8,10]
# class ABC :
#     def function(self,nums):
#         n = len(nums)
#         output = []
#         for i in range(len(nums)):
#             res = abs(sum(nums) - (nums[i]*n))
#             output.append(res)
#         return output
# obj = ABC()
# # obj.function(nums)
# print(obj.function(nums))
class ABC:
    def function(self, nums):
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]+nums[i]
        output = []
        for i in range(len(nums)):
            leftSum = nums[i]*i - prefix[i-1] if i > 0 else 0
            right_element_sum = prefix[-1]- prefix[i]
            rightSum = right_element_sum - (nums[i]*(len(nums)-(i+1)))
            nums[i] = leftSum + rightSum
        return nums


nums = [1, 4, 6, 8, 10]
obj = ABC()
print(obj.function(nums))
