class Solution:
    def minValue(self, s, k):
        mapp = dict()
        for c in s:
            if c not in mapp:
                mapp[c] = 0
            mapp[c] += 1
            
        freqs = sorted(mapp.values(), reverse=True)
        del mapp
        if sum(freqs) <= k:
            return 0
        for i in range(k):
            freqs[0] -= 1
            if freqs[0] == 0:
                freqs.pop(0)
            freqs.sort(reverse=True)
        return self.getValue(freqs)
        
    def getValue(self, freqs):
        return sum([i*i for i in freqs])