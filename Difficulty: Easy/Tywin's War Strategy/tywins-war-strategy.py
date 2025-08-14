import math
class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        for i in range(n):
            arr[i] = 0 if arr[i]%k == 0 else k-arr[i]%k
        arr.sort()
        troops = int(math.ceil(n/2))
        ans = 0
        for i in range(troops):
            ans += arr[i]
        return ans
        