class Solution:
    def substrCount(self, s, k):
        count=0
        for i in range(len(s)-k+1):
            sub=s[i:i+k]
            if len(set(sub)) == k-1:
                count+=1
        return count
        