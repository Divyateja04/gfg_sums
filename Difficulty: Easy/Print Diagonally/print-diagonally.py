class Solution():
    def diagView(self, mat):
        data=[]
        n=len(mat)
        i=0
        for j in range(n):
            start=i
            while(start<n and j>=0):
                data.append(mat[start][j])
                j-=1
                start+=1
        j=n-1
        for i in range(1,n):
            end=j
            while(i<n and end>=0 ):
                data.append(mat[i][end])
                end-=1
                i+=1
        return data

