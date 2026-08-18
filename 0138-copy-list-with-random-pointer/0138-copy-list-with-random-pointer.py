"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hashmap: original node -> copied nodes
        # loop through once to copy nodes and fill up hashmap
        # loop through again to fill up next and random pointers (if not null)
        if not head:
            return None
        
        original_to_copied_nodes = {}
        # loop through once to copy nodes and fill up hashmap
        curr = head
        while curr:
            copy = Node(curr.val)
            original_to_copied_nodes[curr] = copy
            curr = curr.next
        
        # loop through again to fill up next and random pointers (if not null)
        curr1 = head
        while curr1:
            copy = original_to_copied_nodes[curr1]
            copy.next = original_to_copied_nodes.get(curr1.next)
            copy.random = original_to_copied_nodes.get(curr1.random)
            curr1 = curr1.next
        return original_to_copied_nodes[head]



        