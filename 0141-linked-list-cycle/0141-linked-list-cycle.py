

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # move 1 step
            fast = fast.next.next     # move 2 steps

            if slow == fast:
                return True

        return False
        