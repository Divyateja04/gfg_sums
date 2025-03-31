#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr.sort()
        n = len(arr)
        largest = arr[n-1]
        for num in range(n-1,-1,-1):
            if arr[num] != largest:
                return arr[num]
        return -1

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends