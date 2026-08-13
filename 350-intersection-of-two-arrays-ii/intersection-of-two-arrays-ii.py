class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        
        d2 = {}
        for i in nums1:
            d1[i] = d1.get(i,0)+1
        for i in nums2:
            d2[i] = d2.get(i , 0)+1
        result = []
        for key in d1:
            if key in d2:
                count = min(d1[key], d2[key])
                result.extend([key]*count)
        return result


