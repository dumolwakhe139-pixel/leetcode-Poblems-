class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
   
        nums = list(s)
        right = len(nums)-1
        while left < right:
            if  nums[left].isalpha() and nums[right].isalpha():
                nums[left],nums[right] = nums[right], nums[left]
                left+=1
                right-=1
            elif not nums[left].isalpha() and nums[right].isalpha():
                left+=1
            else:
                right-=1
        return "".join(nums)
        
        