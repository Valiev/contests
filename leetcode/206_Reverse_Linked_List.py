# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        l1_head = head
        l2_head = None
        while l1_head:
            (l1_head.next, l2_head, l1_head) = (l2_head, l1_head, l1_head.next)
        return l2_head
