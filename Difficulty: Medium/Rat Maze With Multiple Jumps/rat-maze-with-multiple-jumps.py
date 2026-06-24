class Solution:
	def shortestDist(self, mat):
		n = len(mat)
        jumps = [[0] * n for _ in range(n)]
        def dfs(x: int, y: int) -> bool:
            if mat[x][y]:
                if x == y == n - 1:
                    jumps[x][y] = 1
                    return True
                for d in range(1, mat[x][y] + 1):
                    if ((y1 := y + d) < n and dfs(x, y1)
                        or (x1 := x + d) < n and dfs(x1, y)
                    ):
                        jumps[x][y] = 1
                        return True
                mat[x][y] = 0
            return False
        if not dfs(0, 0):
            return [[-1]]
        return jumps