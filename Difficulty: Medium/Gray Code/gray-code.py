class Solution:
    def graycode(self,n):
        res = []
        for i in range(1 << n):  
            gray = i ^ (i >> 1)
            res.append(format(gray, '0{}b'.format(n)))
        
        return res