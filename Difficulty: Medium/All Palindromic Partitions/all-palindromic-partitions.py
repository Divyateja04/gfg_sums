class Solution:
    def isPalindrome(self,s):
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
        
    def check(self,s,temp,ind,n,dp):
        if ind==n:
            self.res.append(temp[::])
            return
        for i in range(n):
            if ind+i<n and dp[ind][ind+i]:
                temp.append(s[ind:ind+i+1])
                self.check(s,temp,ind+i+1,n,dp)
                del temp[-1]
                
    def palinParts (self, s):
        self.res=[]
        n=len(s)
        dp=[[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=True
                else:
                    dp[i][j]=self.isPalindrome(s[i:j+1])
        self.check(s,[],0,n,dp)
        return self.res

