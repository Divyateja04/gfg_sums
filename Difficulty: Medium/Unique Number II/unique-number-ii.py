#User function Template for python3

from collections import Counter
class Solution:
	def singleNum(self, arr):
		# Code here
		c = Counter(arr)
		l = []
		for i in c.keys():
            if c[i] == 1:
                l.append(i)
        l.sort()
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends