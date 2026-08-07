class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        a = []
        left =0  
        count = 0
        maxlen = 0
        n = len(nums)
        for right in range(n):
            if nums[right]==0:
                count +=1
            while count >k:
                if nums[left] ==0:
                    count -= 1
                left +=1
            maxlen = max(maxlen , right - left +1)
        return maxlen 

        