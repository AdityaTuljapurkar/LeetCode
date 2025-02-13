from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #using count Sort 
        maxVal1 = max(seats)
        count1 = [0]*(maxVal1+1)
        maxVal2 = max(students)
        count2 = [0]*(maxVal2+1)

        # using countsort for seates
        for num in seats :
            count1[num] +=1
        j =0 
        for i in range(maxVal1+1):
            while count1[i] :
                seats[j] = i
                count1[i]-=1 
                j+=1

        for num in students:
            count2[num] +=1
        z=0 
        for i in range (maxVal2+1):
            while count2[i]:
                students[z] = i
                count2[i]-=1
                z+=1

        res :int = 0
        for i in range(len(students)):
            res+= abs(students[i]-seats[i])

        return res  
seats = [4,1,5,9]
students = [1,3,2,6]   
sol = Solution()
print(sol.minMovesToSeat(seats,students))

 
