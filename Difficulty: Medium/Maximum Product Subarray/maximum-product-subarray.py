class Solution:
    def maxProduct(self,arr):
        curr_max = arr[0]
        curr_min = arr[0]
        max_pro = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(arr[i], curr_max*arr[i])
            curr_min = min(arr[i], curr_min*arr[i])
            max_pro = max(curr_max,max_pro)
        return max_pro