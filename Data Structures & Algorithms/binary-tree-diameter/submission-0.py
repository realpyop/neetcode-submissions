# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS throught the tree (diameter = left + right), (height = 1 + max(left, right))
        # Keep track of diameter and result at each level

        # 1) Global variable result to update every iteration
        self.res = 0

        # 2) DFS function RETURNING HEIGHT NOT DIAMETER
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            height = 1 + max(left, right)

            self.res = max(self.res, left + right)
            return height
        
        dfs(root)
        return self.res