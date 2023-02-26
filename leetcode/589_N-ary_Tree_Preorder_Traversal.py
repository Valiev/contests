"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder_recursion(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        acc = [root.val]
        for child in root.children:
            acc += self.preorder_recursion(child)
        return acc

    def preorder(self, root):
        stack = [root]
        values = []
        while stack:
            cur = stack.pop()
            if cur is None:
                break
            values.append(cur.val)
            for child in cur.children[::-1]:
                stack.append(child)
        return values

