class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = [] 
        sum = 0
        for num in nums:
            sum += num
            self.prefix_sum.append(sum)
        

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix_sum[right]
        leftSum = self.prefix_sum[left-1]if left > 0 else 0
        return rightSum - leftSum
    

        