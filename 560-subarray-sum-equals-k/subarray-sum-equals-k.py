class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rs = 0 # This is our prefix sum
        subcnt =  0 #How many subarrays have we seen with sum k 
        seen = {0:1}# HashMap to store prefix sums found so far 
        prefix = [0]
        for i in nums:
            rs+=i
            req = rs -k
            if req in seen:
                subcnt +=seen[req]
            seen[rs] = seen.get(rs , 0)+1
        return subcnt