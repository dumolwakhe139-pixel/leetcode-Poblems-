class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0)+1
        a = sorted(list(d.values()))
        left = 0
        for right in range(1,len(a)):
            if a[right] ==a[left]:
                return False
            left+=1
        return True
        