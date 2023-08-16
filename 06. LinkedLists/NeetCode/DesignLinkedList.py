"""
https://leetcode.com/problems/design-linked-list/

Doubly linked list
"""

class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left, self.right = ListNode(0), ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            index -= 1
            curr = curr.next
        if curr and curr != self.right:
            return curr.val
        return -1
    
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        nextNode = self.left.next
        node.next = nextNode
        node.prev = self.left
        self.left.next = node
        nextNode.prev = node
        
    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        prevNode = self.right.prev
        node.next = self.right
        node.prev = prevNode
        prevNode.next = node
        self.right.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        nextNode = self.left.next
        while curr and index > 0:
            index -= 1
            nextNode = nextNode.next
        if nextNode and index == 0:
            node = ListNode(val)
            prevNode = nextNode.prev
            node.next = nextNode
            node.prev = prevNode
            nextNode.prev = node
            prevNode.next = node
      
    def deleteAtIndex(self, index: int) -> None:
        node = self.left.next
        while node and index > 0:
            node = node.next
            index -= 1
        if node and node != self.right and index == 0:
            node.prev.next = node.next
            node.next.prev = node.prev
            
            

