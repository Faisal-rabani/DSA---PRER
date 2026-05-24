# ID 172 FACTORIAL TRAILING ZEROES

class Solu:
    def trailZe(self,n:int):
        count = 0

        #count the num

        while n >0:
            n = n//5
            count += n
        return count
    
# Testing the function
s = Solu()
print(s.trailZe(5))
