# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init
        if head is None:
            return None
        prev = None
        start = head
        end = start
        count = 0

        while count < n:
            if end is None:
                return head
            end = end.next
            count += 1

        # shift
        while end != None:
            prev = start
            start = start.next
            end = end.next

        if prev is None:
            return head.next

        prev.next = start.next
        return head

