class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def is_feasible(height: int) -> bool:
            changes = [0] * (n + 1)
            curr_diff = used_water = 0
            for i, flower in enumerate(arr):
                curr_diff += changes[i]
                if (h := flower + curr_diff) < height:
                    needed = height - h
                    used_water += needed
                    if used_water > k:
                        return False
                    changes[min(i + w, n)] -= needed
                    curr_diff += needed
            return True
        
        lo = min(arr)
        hi = lo + k
        while lo < hi:
            mid = hi - (hi - lo) // 2
            if is_feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo