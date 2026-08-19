class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    # Doubly linked list needed so that we can efficiently remove nodes in the middle of the linked list in O(1) time. 
    # In LRUCache, each node in linkedlist represents the time of access -> the node could be anywehre in the linked list

class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {} # hashmap: key -> Node
        self.capacity = capacity
        self.head = Node(0, 0) # least recently used
        self.tail = Node(0, 0) # most recently used

        # Link the head and tail up
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        nxt.prev = prev
        prev.next = nxt
    
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]

        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node:
            node = Node(key, value)
            self.key_to_node[key] = node
            self.insert(node)
        else: # already inside the cache, update the value
            node = self.key_to_node[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        if len(self.key_to_node) > self.capacity:
            lru = self.head.next
            prev, nxt = self.head, lru.next
            prev.next, nxt.prev = nxt, prev
            del self.key_to_node[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)