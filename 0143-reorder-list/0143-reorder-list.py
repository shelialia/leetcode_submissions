# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow points to end of first half (even) or middle node (odd)
        # head of second half is slow.next
        prev = None
        curr = slow.next
        slow.next = None # Set end of the result list

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # curr is None, prev is last node
        first, second = head, prev
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        return head



                

