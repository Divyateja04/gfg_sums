from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        dic=defaultdict(int)
        i=0
        j=0
        maxi=-1
        while j<len(s):
            dic[s[j]]+=1
            if len(dic)==k:
                maxi=max(maxi,j-i+1)
            elif len(dic)>k:
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    del dic[s[i]]
                i+=1
            j+=1
        if len(dic)==k:
            maxi=max(maxi,j-i)
        return maxi