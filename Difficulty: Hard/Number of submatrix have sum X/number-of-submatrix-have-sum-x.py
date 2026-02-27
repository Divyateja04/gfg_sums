class Solution:
    def countSquare(self, mat, x):
        n=len(mat)
        m=len(mat[0])
        preSum=[row.copy() for row in mat]
        ans=0
        for i in range(n):
            for j in range(m):
                if i!=0:
                    preSum[i][j]+=preSum[i-1][j]
                if j!=0:
                    preSum[i][j]+=preSum[i][j-1]
                if i!=0 and j!=0:
                    preSum[i][j]-=preSum[i-1][j-1]
                for k in range(1,min(i,j)+2):
                    val=preSum[i][j]
                    val-=(preSum[i-k][j] if i>=k else 0)
                    val-=(preSum[i][j-k] if j>=k else 0)
                    val+=(preSum[i-k][j-k] if i>=k and j>=k else 0)
                    if x==val:
                        ans+=1
        return ans