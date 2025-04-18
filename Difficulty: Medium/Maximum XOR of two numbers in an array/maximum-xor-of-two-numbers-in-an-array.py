#User function Template for python3

class Solution:
    def maxXor(self, arr):
        #code here
        mask,out=0,0
        for i in range(32,-1,-1):
            mask=mask | 1<<i
            f=set([ x & mask for x in arr])
            temp=out |1<<i
            for j in f:
                if j^temp in f:
                    out=temp
        return out

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxXor(arr))
        print("~")

# } Driver Code Ends