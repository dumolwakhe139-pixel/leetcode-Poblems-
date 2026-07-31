class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = x
       
        rev =0
        while(s>0):
            digits = s%10
            rev = (rev *10) + digits
            s = s//10
        if rev==x:
            return True
        else: 
            return False
        