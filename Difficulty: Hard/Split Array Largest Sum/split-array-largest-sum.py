class Solution:
    def splitArray(self, arr, k):
        n = len(arr)
        def isPossible(x):
            s = 0 
            parts = 1 
            for i in range(n):
                if s + arr[i] > x :
                    s = arr[i]
                    parts += 1
                    if parts > k : 
                        return False 
                else:
                    s += arr[i] 
            return True
                    
        l , h = max(arr) , sum(arr) 
        while l <= h : 
            mid = (l + h) // 2 
            if isPossible(mid):
                h =mid-1
            else:
                l = mid+1
        return l 