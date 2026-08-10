class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left  = 0
        
        for i in range (len(word)):
            if word[i] ==ch:
                a =word[:i+1][::-1] +word[i+1:]
                return a
                break
        return word
        