# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case: if node is None return 0
        # DFS
        # if not root:
        #     return 0
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)
        # depth = 1 + max(left_depth, right_depth)
        # return depth



        # BFS
        if not root:
            return 0
        
        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return level
        
