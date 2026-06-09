class Solution:
    def canSeatAllPeople(self, k, seats):
        zeros = 1  
        for s in seats:
            if s:
                if zeros == 0:  
                    return False
                k -= max(0, (zeros - 1) // 2)
                zeros = 0
            else:
                zeros += 1
        k -= zeros // 2
        return k <= 0