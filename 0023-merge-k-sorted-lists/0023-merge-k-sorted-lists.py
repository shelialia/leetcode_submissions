# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode()
        head = dummy
        while heap:
            min_val, min_index, min_node = heapq.heappop(heap)
            dummy.next = min_node
            dummy = dummy.next

            # Add next element to heap, if it exists
            next_node = min_node.next
            if next_node:
                heapq.heappush(heap, (next_node.val, min_index, next_node))
        return head.next