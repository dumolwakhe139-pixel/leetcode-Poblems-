class Solution(object):
    def majorityElement(self, nums):
        freq={}
        n=len(nums)
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key,value in freq.items():
            if value>(n//2):
                return key
            
        