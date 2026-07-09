# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num = 0
        temp = head
        while temp is not None:
            num += 1
            temp = temp.next
        
        num = num - n

        if num == 0:
            return head.next
        
        prev, curr = None, head
        index = 0
        while curr is not None:
            if index == num:
                prev.next = curr.next
                break
            prev, curr = curr, curr.next
            index += 1
        
        return head
            