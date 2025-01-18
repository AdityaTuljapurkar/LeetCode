gain = [-5,1,5,0,-7]
class ABC :
    def function(self,gain):
        res = []
        sum = 0
        res.append(sum)
        for i in range(len(gain)):
            sum += gain[i]
            res.append(sum)
        return max(res)
obj = ABC()
print(obj.function(gain))
