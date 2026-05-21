class Solution:
    def isBitSet(self, n):
        b = bin(n)[2:]
        if '0' in b:
            return False
        return True