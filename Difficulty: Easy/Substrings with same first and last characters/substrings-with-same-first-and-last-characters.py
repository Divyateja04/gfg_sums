class Solution:
	def countSubstring(self, s):
		# code here
		from collections import Counter
		z = 0
		d = {}
	    ct = Counter(s)
	    for value in ct.values():
	        for i in range(value+1):
	            z += i
	            
	            
	    return z

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends