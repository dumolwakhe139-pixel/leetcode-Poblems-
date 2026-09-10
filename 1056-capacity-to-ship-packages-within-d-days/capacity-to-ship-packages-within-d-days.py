def canship(weights ,days_have, capacity ):

    needed = 1
    currentweight = 0
    for w in weights:
        if currentweight + w <=capacity:
            currentweight += w
        else:
            needed +=1
            currentweight = w
    
    return needed <= days_have
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low +high)//2
            if canship(weights, days , mid):
                high =mid
            else :
                low = mid+1
        return low