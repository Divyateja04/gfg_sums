class Solution:
    def caseSort(self,s):
        arr=sorted(list(s))
        i=0
        j=0
        n=len(s)
        s=list(s)
        for k in range(n):
            if arr[k].islower():
                j=k
                break
        for k in range(n):
            if s[k].islower():
                s[k] = arr[j]
                j+=1
            else:
                s[k] = arr[i]
                i+=1
                
        return "".join(s)