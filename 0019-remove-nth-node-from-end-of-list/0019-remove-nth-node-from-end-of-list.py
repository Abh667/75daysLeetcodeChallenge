class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Step 1: Calculate length
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        # Step 2: If head needs to be removed
        if length == n:
            return head.next
        
        # Step 3: Traverse to (length - n - 1)
        temp = head
        for _ in range(length - n - 1):
            temp = temp.next
        
        # Step 4: Delete node
        temp.next = temp.next.next
        
        return head