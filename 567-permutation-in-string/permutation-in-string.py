class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        for i in s1:
            d1[i] = d1.get(i , 0) + 1
        k = len(s1)
        n = len(s2)
        left = 0
        d = {}
        for right in range(n):
            d[s2[right]] = d.get(s2[right] , 0) +1
            if right >=k-1:
                if d == d1:
                    return True 
                d[s2[left]] -=1
                if d[s2[left]] ==0:
                    d.pop(s2[left])
                left +=1
        return False


        