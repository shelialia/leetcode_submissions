class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        previous_group_tail = dummy_head
        current_group_head = head

        while current_group_head:
            current_group_tail = current_group_head

            # Find the kth node in the current group
            for _ in range(k - 1):
                current_group_tail = current_group_tail.next
                if not current_group_tail:
                    break

            # Fewer than k nodes remain
            if not current_group_tail:
                if previous_group_tail:
                    previous_group_tail.next = current_group_head
                break

            next_group_head = current_group_tail.next

            # Reverse the current group
            previous_node = None
            current_node = current_group_head

            while current_node != next_group_head:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            previous_group_tail.next = current_group_tail

            # current_group_head is now the tail of the reversed group
            previous_group_tail = current_group_head
            current_group_head = next_group_head

        return dummy_head.next