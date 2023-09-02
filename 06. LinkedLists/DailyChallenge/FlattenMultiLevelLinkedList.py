"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        stack = []
        while curr:
            while curr and not curr.child:
                curr = curr.next
            if not curr:
                break
            prev = curr.next
            if prev:
                stack.append(prev)
            curr.next = curr.child
            curr.child.prev = curr
            curr = curr.next
        
        tail = dummy
        while tail and tail.next:
            tail = tail.next
            tail.child = None

        while stack:
            node = stack.pop()
            tail.next = node
            node.prev = tail
            while tail and tail.next:
                tail = tail.next
                tail.child = None
        
        return dummy.next