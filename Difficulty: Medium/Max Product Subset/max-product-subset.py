class Solution:
    def findMaxProduct(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0] % (10**9 + 7) if arr[0] > 0 else arr[0]
        count_neg = 0
        count_zero = 0
        prod = 1
        max_neg = float('-inf') 
        for num in arr:
            if num == 0:
                count_zero += 1
                continue
            if num < 0:
                count_neg += 1
                max_neg = max(max_neg, num)
            prod *= num
        if count_zero == n:
            return 0
        if count_neg % 2 != 0:
            if count_neg == 1 and count_zero + count_neg == n:
                return 0
            prod = prod // max_neg
        
        return prod % (10**9 + 7) if prod > 0 else prod   

