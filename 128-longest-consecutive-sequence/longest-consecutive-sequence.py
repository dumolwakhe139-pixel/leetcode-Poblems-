class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        a = set(nums)
        longest  = 0
        for num in a:
            if (num - 1) not in a:
                current_num = num
                count  =1
                while (current_num +1 ) in a:
                    current_num +=1
                    count +=1
                longest  = max(longest , count)
        return longest



    

