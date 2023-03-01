# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self, root, lower, upper):
        if root is None:
            return True
        val = root.val
        if not (lower < val < upper):
            return False
        return self.isValid(root.left, lower, val) and self.isValid(root.right, val, upper)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))
