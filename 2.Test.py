# ID 172 FACTORIAL TRAILING ZEROES

class Solu:
    def tralZo(self, n:int):
        count =0
        
        while n > 0:
            n = n // 5
            count += n
        return count

c = Solu()
print(c.tralZo(15))

