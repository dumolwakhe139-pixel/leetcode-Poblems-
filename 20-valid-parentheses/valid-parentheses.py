class Solution:
    def isValid(self, s: str) -> bool:
        a =     []
        b = "([{"
        C  = ")]}"
        for i in s :
            if i in b :
                a.append(i)
            else :
                if not a:
                    return False 
                else :
                    if i ==')' and a[-1] =="(" or i =="]" and  a[-1]=='[' or i =='}'and a[-1]=='{':
                        a.pop()
                    else :
                        return False
        return not a 
