class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        
        dp = [1] * n  
        
        for i in range(1,n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i],dp[j]+1)
                    
        max_len = max(dp) 
        
        curr_len = max_len
        LIS = []
        
        for i in range(n-1,-1,-1):
            if curr_len == dp[i]:
                LIS.append(arr[i])
                curr_len -= 1
                
        LIS = LIS[::-1]  
        return sum(arr) - sum(LIS)