class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1 
        total = 0
        n
        while(n>0):
            digits= n %10
            product *= digits
            total +=digits
            n =n//10
        diff = product - total
        return diff


        