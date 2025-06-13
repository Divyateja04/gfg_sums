#User function Template for python3

import math
class Solution:
    def kokoEat(self,arr,k):
        l,r = 1, max(arr)
        
        def helper(mid):
            count = 0
            
            for i in arr:
                count += math.ceil(i/mid)
            
            return count <= k
        
        ans = 0
        while l<=r:
            mid = l + (r-l)//2
            if helper(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid+1
        
        return ans