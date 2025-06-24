class Solution:
    def maxSubseq(self, s, k):
        result= []
        for ch in s:
            while result and result[-1] < ch and k > 0:
                result.pop()
                k-=1
            result.append(ch)
        
        while k > 0:
            result.pop()
            k-=1
        return ''.join(result)
        
