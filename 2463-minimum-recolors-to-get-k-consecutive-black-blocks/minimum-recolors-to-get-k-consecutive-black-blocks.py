class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left  = 0
        count_op = 1
        count =0
        min_recolors = float('inf')
        for right in range (len(blocks)):
            if blocks[right] == 'W':
                count +=1
            if (right - left +1) ==k:
                min_recolors = min(min_recolors, count)
                if blocks[left] == 'W':
                    count -=1
                left +=1
        return min_recolors
            

            
                

        