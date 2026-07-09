# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        curr1, curr2 = l1, l2
        pos1, pos2 = 1, 1
        
        while curr1 is not None:
            num1 += curr1.val * pos1
            pos1 *= 10
            curr1 = curr1.next

        while curr2 is not None:
            num2 += curr2.val * pos2
            pos2 *= 10
            curr2 = curr2.next
        
        total = num1 + num2

        if total == 0:
            return ListNode(0)

        node = ListNode()
        curr = node

        while total > 0:
            curr.next = ListNode(total % 10)
            curr = curr.next
            total //= 10

        return node.next