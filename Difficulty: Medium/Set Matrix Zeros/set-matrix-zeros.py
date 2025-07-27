class Solution:
    def setMatrixZeroes(self, mat):
        isRowZero=False
        n,m=len(mat),len(mat[0])
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    if i:
                        arr[i][0]=0
                    else:
                        isRowZero=True
                    arr[0][j]=0
        for i in range(1,n):
            for j in range(1,m):
                if arr[i][0]==0 or arr[0][j]==0:
                    arr[i][j]=0
        if arr[0][0]==0:
            for i in range(1,n):
                arr[i][0]=0
        if isRowZero:
            for j in range(m):
                arr[0][j]=0
        