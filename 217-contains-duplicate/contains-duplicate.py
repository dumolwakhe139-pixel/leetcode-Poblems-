class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],0)+1
        if max(d.values())==1:
            return False
        else :
            return True
            
        