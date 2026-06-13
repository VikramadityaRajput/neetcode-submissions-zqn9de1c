class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #maps keys to nodes
        self.right, self.left = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node): # pointer helper functions
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache: #put it in the back of line because MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # if it already exists we have to get rid of and replace it
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key]) 

        if (len(self.cache) > self.cap):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
