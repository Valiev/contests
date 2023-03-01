# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_next = root
        p_val = p.val
        q_next = root
        q_val = q.val
        prev = root
        while p_next == q_next:
            prev = p_next
            if p_val > prev.val:
                p_next = p_next.right

            if p_val < prev.val:
                p_next = p_next.left

            if q_val > prev.val:
                q_next = prev.right

            if q_val < prev.val:
                q_next = q_next.left

        return prev
