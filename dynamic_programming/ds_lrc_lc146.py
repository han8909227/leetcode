# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


class Node(object):
    """Simple Node classs for dll."""

    def __init__(self, key, value):
        """."""
        self.key = key
        self.value = value
        self.prev, self.next = None, None


class LRUCache(object):
    """."""

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.dict = {}
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            node.value = value
            self._insert(node)
        else:
            if self.size == self.capacity:
                discard = self.tail.prev
                self._remove(discard)
                del self.dict[discard.key]
                self.size -= 1
            node = Node(key, value)
            self.dict[key] = node
            self._insert(node)
            self.size += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def _insert(self, node):
        """
        :type node: Node
        :rtype: void
        Insert after head: head is always -1 node
        """
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        """
        :type node: Node
        :rtype: void
        Remove node from the dll (always in the middle)
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next, node.prev = None, None


if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    assert lru_cache.get(0) == -1
    assert lru_cache.get(1) == 1
    lru_cache.put(1, 10)
    assert lru_cache.get(1) == 10
    lru_cache.put(4, 4)
    assert lru_cache.get(2) == -1
