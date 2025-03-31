class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        s=arr[0]
        res=arr[0]
        for i in range(1,len(arr)):
            s=max(s+arr[i],arr[i])
            res=max(s,res)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends