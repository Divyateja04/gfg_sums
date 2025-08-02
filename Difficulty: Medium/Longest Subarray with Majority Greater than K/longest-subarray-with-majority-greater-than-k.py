class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        trans = [1 if x > k else -1 for x in arr]
        prefix = 0
        first_occurrence = {0: -1}
        max_len = 0
        for i in range(n):
            prefix += trans[i]
            if prefix > 0:
                max_len = i + 1
            if (prefix - 1) in first_occurrence:
                prev_index = first_occurrence[prefix - 1]
                max_len = max(max_len, i - prev_index)
            if prefix not in first_occurrence:
                first_occurrence[prefix] = i
        
        return max_len