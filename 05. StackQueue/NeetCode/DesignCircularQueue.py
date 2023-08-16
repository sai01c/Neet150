"""
https://leetcode.com/problems/design-circular-queue/

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.length = 0
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.length < self.k:
            prevNode = self.right.prev
            node = ListNode(value)
            node.next = self.right
            node.prev = prevNode
            prevNode.next = node
            self.right.prev = node
            self.length += 1
            return True
        return False
        
    def deQueue(self) -> bool:
        if self.length > 0:
            node = self.left.next
            nextNode = node.next
            self.left.next = nextNode
            nextNode.prev = self.left
            self.length -= 1
            return True
        return False

    def Front(self) -> int:
        if self.length > 0:
            return self.left.next.val
        return -1
    
    def Rear(self) -> int:
        if self.length > 0:
            return self.right.prev.val
        return -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k
