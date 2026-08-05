class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        count = 0 
        a = []
        for i in range (len(nums)):
            if nums[i] ==1:
                count+=1
            else :
                a.append(count)
                count = 0
        return max(a)
        