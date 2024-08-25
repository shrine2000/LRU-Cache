class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: Node | None = None
        self.prev: Node | None = None


# deletion takes place near to head
# insertion takes place near to tail
# most recently used item will near tail and least recently used item will be near head


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}  # hold keys and their corresponding nodes
        self.head: Node = Node(0, 0)  # dummy head
        self.tail: Node = Node(0, 0)  # dummy tail
        self.head.next = (
            self.tail
        )  # prev of dummy head points to NULL and next point to dummy tail
        self.tail.prev = (
            self.head
        )  # prev of dummy tail points to head, next point to NULL

    def _remove(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node: Node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            # remove the least recently used node which is right after the head
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
        # add new node or update the existing node
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node

