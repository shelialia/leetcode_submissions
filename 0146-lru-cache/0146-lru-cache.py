class LRUCache:
    # Keep track of capacity
    # Keep a ordereddict (lru elem in front)
    # get -> check if key exists. use move_to_end to make key mru
    # put -> check if key exists. if exists, update the value. otherwise, create it. use move_to_end to make key mru. if exceed capacity, evict from head

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value

        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)