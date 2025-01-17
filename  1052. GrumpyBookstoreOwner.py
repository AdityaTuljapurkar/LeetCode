class ABC :
    def function(self,customer,grumpy,k):
        start =0 
        end = 0
        currVal= 0
        maxVal = 0
        minSatisfiedCustomer = 0
        i = 0

        for  i in range(len(customer)):
            minSatisfiedCustomer +=(1-grumpy[i])*customer[i]
        for end in range(k):
            currVal += (grumpy[end])*customer[end]
            maxVal = max(maxVal,currVal)


        # while end < len(customer):
        #     currVal += (grumpy[end])*customer[end]
        #     currVal -= grumpy[start]*customer[start]
        #     start+=1
        #     end+=1
        #     maxVal = max(maxVal,currVal)

        for end in range(k,len(customer)):
            currVal += (grumpy[end])*customer[end]
            currVal -= grumpy[start]*customer[start]
            start+=1
            maxVal = max(maxVal,currVal)

        return maxVal+minSatisfiedCustomer

customer = [1,0,1,2,1,1,7,5]
grumpy =[0,1,0,1,0,1,0,1]
k = 3
obj = ABC()
print(obj.function(customer,grumpy,k))  # Output: 16



