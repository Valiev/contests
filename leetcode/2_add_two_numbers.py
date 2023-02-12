# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def build(self, l1, l2, extra=0):
        ls = (l1, l2)
        if ls == (None, None):
            if extra == 0:
                return None
            else:
                return ListNode(val=extra)

        value = sum(l.val for l in ls if l is not None)
        value += extra
        if value > 9:
            value -= 10
            extra = 1
        else:
            extra = 0

        nexts = [l for l in ls if l is None] + [l.next for l in ls if l is not None]

        l = ListNode(
            value,
            self.build(*nexts, extra)
        )
        return l


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.build(l1, l2, 0)
