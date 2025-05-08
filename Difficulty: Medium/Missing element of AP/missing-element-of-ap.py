#User function Template for python3

class Solution:
    def findMissing(self, arr):
        # code here
        for i in range(1,len(arr) - 1):
            mid = (arr[i - 1] + arr[i + 1])//2
            if mid != arr[i]:
                return arr[i] + (arr[i] - arr[i - 1])
        return arr[-1] + (arr[-1] - arr[-2])


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends