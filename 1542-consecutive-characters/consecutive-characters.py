class Solution:
    def maxPower(self, s: str) -> int:
        count = 1 
        maxcount = 1
        a = []
        for i in range (1,len(s)):
            if s[i] == s[i-1]:
                count +=1
            else :
                a.append(count)
                count =1
        a.append(count)
        return max(a)
        