class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        left = 0
        n = len(nums)
        rsum = 0
        a = []
        duplicates = 0
        for right in range(n):
            rsum +=nums[right]
            d[nums[right]] = d.get(nums[right],0)+1
            if d[nums[right]]==2:
                duplicates +=1
            if right >= k-1:
                if duplicates == 0:
                    a.append(rsum)
                d[nums[left]] -=1
                if d[nums[left]]==1:
                    duplicates -=1
                if d[nums[left]] ==0:
                    del d[nums[left]]
                rsum -= nums[left]
                left+=1
        return max(a) if a else 0
        