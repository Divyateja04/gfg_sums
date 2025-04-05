#User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        rows=len(grid)
        cols=len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        vectors =[(0, 1),(1, 0),(-1, 0),(0, -1),(-1, 1),(1, 1),(1, -1),(-1, -1)]

        def dfs(row,col):
            stack=[(row,col)]
            visited[row][col]=True
            while stack:
                r,c=stack.pop()
                for x,y in vectors:
                    new_row,new_col=r+x,c+y
                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]=='L' and not visited[new_row][new_col]:
                        visited[new_row][new_col]=True
                        stack.append((new_row,new_col))
        island=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='L' and not visited[i][j]:
                    dfs(i,j)
                    island+=1
        return island

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends