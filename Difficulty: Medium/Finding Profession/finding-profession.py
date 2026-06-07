class Solution:
    def profession(self, level, pos):
        return ("Engineer" if bin(pos - 1).count('1')%2==0 else "Doctor")