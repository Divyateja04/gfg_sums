#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
    	# code here 
    	for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==x:
                    return True
        return False 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends