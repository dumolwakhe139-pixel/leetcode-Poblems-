class Solution:
    def removeDuplicates(self, s: str) -> str:
        a = []
     
        for i in s:
            if not a:
                a.append(i)
            elif a[-1]== i:
                a.pop()
            else :
                a.append(i)
        return "".join(a)        