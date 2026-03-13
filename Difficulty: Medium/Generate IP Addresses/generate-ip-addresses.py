class Solution:
    def generateIp(self, s):
        lth=len(s)
        ret=[]
        res=[]
        def dfs(ix=0):
            nonlocal s,lth,ret,res
            if len(res)>4:
                return
            if ix>=lth:
                if len(res)!=4:
                    return
                ret.append('.'.join(list(map(str,res))))
                return
            ve=int(s[ix])
            res.append(ve)
            dfs(ix+1)
            res.pop()
            if res and res[-1]>0:
                if 10*res[-1]+ve<256:
                    tmp=res[-1]
                    res[-1]=10*res[-1]+ve
                    dfs(ix+1)
                    res[-1]=tmp
        dfs()
        return ret