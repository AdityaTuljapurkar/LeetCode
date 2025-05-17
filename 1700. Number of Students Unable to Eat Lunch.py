from typing import List 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq_s = [0,0] 
        res = len(students)
        for i in range(res):
            freq_s[students[i]] +=1 
        
        for s in sandwiches :
            if freq_s[s] > 0 :
                res-=1 
                freq_s[s] -=1 
                
            else : 
                return res 
            
        return res 
        

sol = Solution()
print(sol.countStudents([1,1,1,0,0,1],[1,0,0,0,1,1]))
