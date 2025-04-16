class Solution:
    def findMinCycle(self, V, edges):
        # code here
        INF = float('inf')
        dist = [[INF] * V for _ in range(V)]
        adj = [[INF] * V for _ in range(V)]
        for u, v, w in edges:
            if w < adj[u][v]:  # keep minimum weight if multiple edges
                adj[u][v] = w
                adj[v][u] = w
                dist[u][v] = w
                dist[v][u] = w

        min_cycle = INF
        for k in range(V):
            # Check for cycles through vertex k
            for i in range(k):
                for j in range(i):
                    if dist[i][j] != INF and adj[i][k] != INF and adj[k][j] != INF:
                        cycle_weight = dist[i][j] + adj[i][k] + adj[k][j]
                        min_cycle = min(min_cycle, cycle_weight)
            for i in range(V):
                for j in range(V):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return min_cycle if min_cycle != INF else -1

        



#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        obj = Solution()
        res = obj.findMinCycle(V, edges)

        print(res)


if __name__ == "__main__":
    main()

# } Driver Code Ends