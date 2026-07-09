# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []

        curr = head
        while curr is not None:
            lst.append(curr)
            curr = curr.next

        i, j = 0, len(lst) - 1
        while i < j:
            lst[i].next = lst[j]
            i += 1
            if i >= j:
                break
            lst[j].next = lst[i]
            j -= 1
        lst[i].next = None