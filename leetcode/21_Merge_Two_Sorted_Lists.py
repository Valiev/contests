# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode()
        head = fake_head
        while list1 or list2:
            if list1 is None:
                head.next = list2
                break
            if list2 is None:
                head.next = list1
                break
            v1, v2 = list1.val, list2.val
            if v1 <= v2:
                head.next = list1
                head = head.next
                list1 = list1.next
            else:
                head.next = list2
                head = head.next
                list2 = list2.next
        return fake_head.next
