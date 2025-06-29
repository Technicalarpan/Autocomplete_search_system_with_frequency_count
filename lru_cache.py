class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return True
        return False

    def put(self, key):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove LRU
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def get_all(self):
        # Return list of keys from most recent to least
        result = []
        current = self.tail.prev
        while current != self.head:
            result.append(current.key)
            current = current.prev
        return result
