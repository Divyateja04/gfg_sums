#User function Template for python3
class Solution:
    def findLength(self, color, radius):
        stack=[]
        for i,j in zip(color,radius):
            if stack and stack[-1]==(i,j):
                stack.pop()
            else:
                stack.append((i,j))
                
        return len(stack)