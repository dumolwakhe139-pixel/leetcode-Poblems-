class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiouAEIOU"
        nums = list(s)
        right = len(nums)-1
        left = 0
        while left < right:
            if nums[left] in vowel and nums[right] in vowel:
                nums[left] ,nums[right] = nums[right], nums[left]
                left +=1
                right-=1
            elif nums[left] in vowel and not nums[right] in vowel:
                right -=1
            else:
                left+=1
        return "".join(nums)

        