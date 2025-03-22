class Solution:
    def maxValue(self, arr):
        def solve(start, end):
            taken = not_taken = 0
            for i in range(start, end):
                taken, not_taken = not_taken + arr[i], max(taken, not_taken)
            return max(taken, not_taken)
        
        n = len(arr)
        return max(solve(1, n), solve(0, n - 1))


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends