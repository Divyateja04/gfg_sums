class Solution:
    def getLongestPrefix(self, s):
        n = len(s)
        if n == 1:
            return -1 
        z = [0] * n
        left, right = 0, 0
        for i in range(1, n):
            if i <= right:
                z[i] = min(right - i + 1, z[i - left])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > right:
                left, right = i, i + z[i] - 1
        for length in range(n - 1, 0, -1):
            if z[length] >= n - length:
                return length
        return -1
        
