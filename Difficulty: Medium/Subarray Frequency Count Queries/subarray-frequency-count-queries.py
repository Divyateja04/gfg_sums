import bisect
from collections import defaultdict
class Solution:
    def freqInRange(self, arr, queries):
        map=defaultdict(list)
        n=len(arr)
        for i in range(n):
            map[arr[i]].append(i)
        ans=[]
        for l,r,x in queries:
            if not map[x]:
                ans.append(0)
                continue
            pos=map[x]
            left=bisect.bisect_left(pos,l)
            right=bisect.bisect_right(pos,r)
            ans.append(right-left)
        return ans