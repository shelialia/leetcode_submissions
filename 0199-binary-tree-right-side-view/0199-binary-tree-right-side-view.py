# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Find level ordering of nodes
        # Instead of returning the level order, we append the rightmost node in each level
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            curr_level_len = len(queue)
            for i in range(curr_level_len):
                curr_level = []
                curr_node = queue.popleft()
                if i == curr_level_len - 1:
                    res.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return res
        