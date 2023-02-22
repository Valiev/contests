class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        a, b, c = None, head, head.next
        head = None
        while True:
            # rearrange
            if a is not None:
                a.next = c
            b.next = c.next
            c.next = b
            if head is None:
                head = c

            # shift
            a = b
            b = a.next
            if b is None:
                break
            c = b.next
            if c is None:
                break
        return head






