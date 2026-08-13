# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head
        while fast and fast.next: # Only need to check Null condition for fast, because fast moves faster and would reach the end first
            slow = slow.next # Move 1 node each time
            fast = fast.next.next # Move 2 nodes each time
            if slow == fast:
                return True
        return False