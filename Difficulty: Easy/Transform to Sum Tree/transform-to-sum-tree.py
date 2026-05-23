class Solution:
    def toSumTree(self, root):
        def solve(node):
            if node is None:
                return 0
            left_tree_sum = solve(node.left)
            right_tree_sum = solve(node.right)
            curr_node_val =  node.data
            node.data = left_tree_sum + right_tree_sum
            return curr_node_val + node.data
        solve(root)