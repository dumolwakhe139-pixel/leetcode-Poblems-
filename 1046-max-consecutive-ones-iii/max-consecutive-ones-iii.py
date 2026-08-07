class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        a = []
        left =0  
        count = 0
        n = len(nums)
        for right in range(n):
            if nums[right]==0:
                count +=1
            while count >k:
                if nums[left] ==0:
                    count -= 1
                left +=1
            a.append(right - left + 1)
        return max(a)

        