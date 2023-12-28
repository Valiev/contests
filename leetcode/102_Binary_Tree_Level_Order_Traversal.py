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


class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None

        def next_level(level):
            acc = []
            for node in level:
                if node is None:
                    continue
                if node.left is not None:
                    acc.append(node.left)
                if node.right is not None:
                    acc.append(node.right)
            return acc

        acc = []
        stack = [[root]]
        while stack:
            level = stack.pop()
            if not level:
                break
            acc.append([node.val for node in level])
            stack.append(next_level(level))
        return acc

