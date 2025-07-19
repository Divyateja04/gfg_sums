class Solution:
    def vowelCount(self, s):
        dic = {}
        for i in s:
            if i in'aeiou':
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
        values=list(dic.values())
        keys=list(dic.keys())
        factorial=1
        for i in range(1,len(keys)+1):
            factorial*=i
        for i in range(len(values)):
            if values[i]>1:
                factorial*=values[i]
                
        if dic:
            return factorial
        return 0