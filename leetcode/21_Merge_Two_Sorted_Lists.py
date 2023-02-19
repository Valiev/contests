# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        node = list1
        next_l1 = list1.next
        next_l2 = list2
        if list1.val > list2.val:
            node = list2
            next_l1 = list1
            next_l2 = list2.next
        node.next = self.mergeTwoLists(next_l1, next_l2)
        return node
