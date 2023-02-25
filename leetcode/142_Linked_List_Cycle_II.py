# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        # detect cycle
        slow = head
        fast = head
        cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycle = True
                break

        if not cycle:
            return None

        # find cycle ingress
        # the trick:
        # X - path to ingress
        # Y - pos from ingress to meeting point of SLOW and FAST
        # Z - path from Y to the end of list
        # ----
        # Slow path: X + Y
        # Fast path: X + Y + Z + Y
        # Since Fast path 2 times bigger then slow, then
        # 2 (x + y) = x + y + z + y
        # 2x + 2y = x + 2y + z
        # x = z
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
