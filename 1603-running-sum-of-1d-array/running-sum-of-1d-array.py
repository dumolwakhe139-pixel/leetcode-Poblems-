class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = 0
        a = []
        for i in range (len(nums)):
            rs+=nums[i]
            a.append(rs)
        return a

        