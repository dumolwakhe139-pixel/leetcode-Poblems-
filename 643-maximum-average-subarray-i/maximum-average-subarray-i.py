class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        maxAverage = -10000000
        right = 0
        left  = 0
        currentsum = 0
        for right in range(n):
            currentsum +=nums[right]
            if right >= k-1:
                avg = currentsum / k
                maxAverage = max(avg , maxAverage)
                currentsum -=nums[left]
                left += 1
        return maxAverage
            