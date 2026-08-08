class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = []
        left  = 0
        d = {}
        for right in range (len(s)):
            d[s[right]] = d.get(s[right] , 0) + 1
            while d[s[right]] >1:
                d[s[left]] -=1
                left +=1
            c = right -left + 1
            a.append(c)
        if len(a) ==0:
            return 0
        return max(a)
        
        