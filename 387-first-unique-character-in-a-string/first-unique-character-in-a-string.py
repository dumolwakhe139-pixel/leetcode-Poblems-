class Solution(object):
    def firstUniqChar(self, s):
        freq={}
        found=False
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        for i in range(len(s)):
            if s[i] in freq:
                if freq[s[i]]==1:
                    found=True
                    return i
        if not found:
            return -1
            
                
        