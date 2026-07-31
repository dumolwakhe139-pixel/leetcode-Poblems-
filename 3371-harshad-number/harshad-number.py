class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = x
        total = 0
        while(n !=0):
            digits = n%10
            total += digits
            n//=10
        if x%total ==0:
            return total
        else :
            return -1

    
        