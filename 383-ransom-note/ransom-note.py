class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for ch in magazine:
            if ch in d.keys():
                d[ch]+= 1
            else:
                d[ch]=1
        for ch in ransomNote:
            if ch not in d.keys():
                return False
            else:
                if d[ch] > 0:
                    d[ch]-=1
                else:
                     return False
        return True 

        