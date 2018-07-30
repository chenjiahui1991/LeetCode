class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = dict()
        self.capacity = capacity

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return self.dict[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            node.val = value
            return
        if len(self.dict) < self.capacity:
            node = Node(key, value)
            self.dict[key] = node
            self._add(node)
            return
        del self.dict[self.head.next.key]
        self._remove(self.head.next)
        node = Node(key, value)
        self.dict[key] = node
        self._add(node)


cache = LRUCache(2)

cache.put(2, 1)
cache.put(2, 2)
print(cache.get(2))
