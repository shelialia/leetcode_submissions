# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, biggest_val):
            nonlocal count
            if not node:
                return
            if node.val >= biggest_val:
                count += 1
                biggest_val = node.val

            dfs(node.left, biggest_val)
            dfs(node.right, biggest_val)
            
        dfs(root, root.val)
        return count