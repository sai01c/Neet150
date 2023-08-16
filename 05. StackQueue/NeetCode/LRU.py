"""
https://leetcode.com/problems/lru-cache/

Approach - maintain dic and queue. append latest value to the queue. pop lru from left
this is very inefficient compared to doubly linked list solution.

tc - O(1)
sc - O(capacity)

"""

from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key):
        if key in self.cache:
            # Move the key to the end of the queue
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            # Update the value and move the key to the end of the queue
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            # Add the new key-value pair to the cache and the end of the queue
            if len(self.cache) == self.capacity:
                # Remove the least recently used key from the cache and the front of the queue
                lru_key = self.queue.popleft()
                del self.cache[lru_key]
            self.cache[key] = value
            self.queue.append(key)

