# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_sub(orig, sub):
            if (orig, sub) == (None, None):
                return True
            if (orig is None) or (sub is None):
                return False
            if orig.val != sub.val:
                return False
            return check_sub(orig.left, sub.left) and check_sub(orig.right, sub.right)

        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue

            if check_sub(node, subRoot):
                return True
            else:
                stack.append(node.left)
                stack.append(node.right)

        return False
