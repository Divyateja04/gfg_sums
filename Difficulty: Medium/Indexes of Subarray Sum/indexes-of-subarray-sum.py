#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        start,s =0,0
    
        for i in range(len(arr)):
            s += arr[i]
            while s > target:
                s -=arr[start]
                start +=1
                
            if s == target:
                return [start+1, i+1]
                    
        return [-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends