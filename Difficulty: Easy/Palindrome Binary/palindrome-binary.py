class Solution:
    def isBinaryPalindrome(self, n):
        binary = bin(n)[2:]
        if binary == binary[::-1]:
            return 1
        return 0