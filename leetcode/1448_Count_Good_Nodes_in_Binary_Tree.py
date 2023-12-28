# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if node is None:
                return 0
            counter = 0
            if node.val >= max_val:
                counter += 1
            return counter + dfs(node.left, max(max_val, node.val)) + dfs(node.right, max(max_val, node.val))
        if root is None:
            return None
        return dfs(root, root.val)


    def goodNodesBFS(self, root: TreeNode) -> int:
        if root is None:
            return None

        stack = [(root, root.val)]
        counter = 0
        while stack:
            node, max_val_so_far = stack.pop()
            if node is None:
                continue
            if node.val >= max_val_so_far:
                counter += 1
            stack.append((node.left, max(max_val_so_far, node.val)))
            stack.append((node.right, max(max_val_so_far, node.val)))
        return counter


#   2
#. x 4
#.    10 8
#.       4
