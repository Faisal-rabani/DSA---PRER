# ID 172 FACTORIAL TRAILING ZEROES

class Solu:
    def traliZ(self,n:int):

        cou =0

        while n > 0:
            n = n// 5
            cou += n
        return cou
    
c = Solu()
print(c.traliZ(9))