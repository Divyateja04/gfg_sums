class Solution:
	def countPairs(self, mat1, mat2, x):
		n = len(mat1) * len(mat1[0])
		i, j = 0, n-1
		
		ret = 0
		while i < n and j >= 0:
		    r1, c1 = divmod(i, len(mat1[0]))
		    r2, c2 = divmod(j, len(mat1[0]))
		    
		    s = mat1[r1][c1] + mat2[r2][c2]
		    if s < x:
		        i += 1
		    elif s > x:
		        j -= 1
		    else:
		        ret += 1
		        i += 1
		        j -= 1
		 
	    return ret