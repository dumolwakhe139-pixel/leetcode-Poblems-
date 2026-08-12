class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
       
        ans = []
        for i in range(len(nums)):
            pro = nums[i]*nums[i]
            ans.append(pro)
        return sorted(ans)
        