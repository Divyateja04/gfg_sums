class Solution:
    def countValid(self, n, arr):
        f = set(arr)
        allowed = set(range(10)) - f
        if n == 1:
            total = 9  
            total_without = len([d for d in allowed if 1 <= d <= 9])
        else:
            total = 9 * pow(10, n-1) 
            if not allowed:
                total_without = 0
            else:
                first_digit_opts = len(allowed) - (1 if 0 in allowed else 0)
                total_without = first_digit_opts * pow(len(allowed), n-1)
                    
        return total - total_without