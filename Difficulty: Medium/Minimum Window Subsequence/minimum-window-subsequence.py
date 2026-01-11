class Solution:
    def minWindow(self, s1, s2):
        # Code here
        n=len(s1)
        m=len(s2)
        mini=float('inf')
        ans=""
        for i in range(n): 
            if s1[i]==s2[0]: # forward pass to pick the matched characters
                p1=i
                p2=0
                while p1<n and p2<m:
                    if s1[p1]==s2[p2]:
                        p2+=1
                    p1+=1
                if p2==m:  # found the subsequence
                    end=p1-1
                    p2=m-1
                    while end>=i: # for the minimum subsequence
                        if s1[end]==s2[p2]:
                            p2-=1
                        if p2<0:
                            break
                        end-=1
                    start=end
                    lgt=p1-start # the length is initial index-end
                    while lgt<mini:
                        mini=lgt
                        ans=s1[start:start+lgt] # the final answer
        return ans