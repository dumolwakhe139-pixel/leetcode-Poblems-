class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        right =0
        left = 0
        sum1 =0
        count = 0
        a  =[]
        for right in range (n):
            sum1 += arr[right]
            if right >= k-1:
                avg = sum1//k
                a.append(avg)
                sum1 -=arr[left]
                left +=1
        for i in range (len(a)):
            if a[i] >= threshold:
                count +=1
        return count
        