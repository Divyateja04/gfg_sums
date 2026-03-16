class Solution:
    def Count(self, root, k, dict1, sum1):
        if not root:
            return
        sum1 += root.data
        diff = sum1 - k
        if diff == 0:
            self.count += 1
        if diff in dict1:
            self.count += dict1[diff]

        dict1[sum1] = dict1.get(sum1, 0) + 1
        self.Count(root.left, k, dict1, sum1)
        self.Count(root.right, k, dict1, sum1)
        
        dict1[sum1] -= 1
        if dict1[sum1] == 0:
            del dict1[sum1]
            
    def countAllPaths(self, root, k):
        self.count = 0
        dict1 = {}
        self.Count(root, k, dict1, 0)
        return self.count