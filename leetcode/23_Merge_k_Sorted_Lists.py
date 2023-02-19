# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge2(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val < list2.val:
        curnode = list1
        list1 = list1.next
    else:
        curnode = list2
        list2 = list2.next

    head = curnode
    while (list1, list2) != (None, None):
        if list1 is None:
            curnode.next = list2
            curnode = list2
            break

        if list2 is None:
            curnode.next = list1
            curnode = list1
            break

        if list1.val < list2.val:
            curnode.next = list1
            curnode = list1
            list1 = list1.next
        else:
            curnode.next = list2
            curnode = list2
            list2 = list2.next

    return head


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        sorted_list = lists.pop()
        while lists:
            sorted_list = merge2(sorted_list, lists.pop())
        return sorted_list
