class Solution:
    def areIsomorphic(self, s1, s2):
        f1,f2={},{}
        n=len(s1)
        for i in range(n):
            if f1.get(s1[i],s2[i])!=s2[i]:
                return False
            else:
                f1[s1[i]]=s2[i]
            if f2.get(s2[i],s1[i])!=s1[i]:
                return False
            else:
                f2[s2[i]]=s1[i]
        return True