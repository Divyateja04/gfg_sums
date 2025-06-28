from bisect import bisect_right
class Solution:
    def countLessEq(self, a, b):
        b.sort()
        return [bisect_right(b,val)for val in a]