class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
       
        for i in range (len(s)):
            if s[i].isalnum():
                count += 1
                last = count
            else :
                count = 0
        return last 
      