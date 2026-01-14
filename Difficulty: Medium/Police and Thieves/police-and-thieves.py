class Solution:
    def catchThieves(self, arr, k):
        try:
            t=arr.index('T')
            p=arr.index('P')
        except:
            return 0
        ret=0
        while 1:
            if abs(p-t)<=k:
                ret+=1
                try:
                    t=arr.index('T',t+1)
                    p=arr.index('P',p+1)
                except:
                    return ret
            elif t<p:
                try:
                    t=arr.index('T',t+1)
                except:
                    return ret
            else:
                try:
                    p=arr.index('P',p+1)
                except:
                    return ret