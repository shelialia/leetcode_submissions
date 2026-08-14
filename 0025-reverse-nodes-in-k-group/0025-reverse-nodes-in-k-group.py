# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        to_reverse_head = head
        to_reverse_tail = None
        result_head = None
        while to_reverse_head:
            start, end = to_reverse_head, to_reverse_head

            for i in range(k - 1):
                end = end.next
                if not end:
                    break
                    
            if not end:
                to_reverse_tail.next = start
                break
            
            next_group = end.next
            to_reverse_head = next_group

            prev = None
            curr = start

            if not result_head:
                result_head = end

            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            if to_reverse_tail:
                to_reverse_tail.next = end

            to_reverse_tail = start


        return result_head

                

                