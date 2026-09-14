class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
     
        d = {}
        for i in range (len(nums)):
            num = nums[i]
            if num in d and i - d[num]<= k:
                return True
            d[num ] = i
        return False
