class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = []
        runningsum = 0 
        for i in range(len(nums)):
            runningsum+= nums[i]
            a.append(runningsum)
        return a          


        