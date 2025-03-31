#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        # code here
       n=len(arr)+1#for getting lenght of array
       total_sum_of_array=sum(arr)#using function to get sum of aray
       Total_For_arr=int((n*(n + 1))/2)#Implementing the n natural number formula 
       return (Total_For_arr-total_sum_of_array)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends