# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level = 0
        stack = [(level, root)]
        levels = []
        while stack:
            lvl, node = stack.pop()
            while lvl + 1 > len(levels):
                levels.append([])
            levels[lvl].append(node.val)
            if node.right is not None:
                stack.append((lvl+1, node.right))
            if node.left is not None:
                stack.append((lvl+1, node.left))
        return levels

