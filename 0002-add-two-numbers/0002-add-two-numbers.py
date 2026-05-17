# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()   # Dummy node for result list
        current = dummy
        carry = 0

        # Traverse both linked lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Sum of digits + carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
        