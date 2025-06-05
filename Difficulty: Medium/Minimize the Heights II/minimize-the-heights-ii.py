#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()  # Sorting the list
        n = len(arr)
        ans = arr[-1] - arr[0]  # Initial difference
        smallest = arr[0] + k
        largest = arr[-1] - k
        
        for i in range(n - 1):
            maxi = max(largest, arr[i] + k)
            mini = min(smallest, arr[i + 1] - k)

            if mini < 0:
                continue

            ans = min(ans, maxi - mini)

        return ans