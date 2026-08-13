# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for i in range(n): # Move fast n steps ahead of slow
            fast = fast.next
        if not fast: # linked list of length 1; head.next is null
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        # Fast points to None of it exists now
        slow.next = slow.next.next # Skip the node to remove
        return head