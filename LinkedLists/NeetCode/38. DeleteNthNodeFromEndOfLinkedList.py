"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

Approach: create two pointers left and right
idea is to have the diff of n+1 between them
move right by n times 
and then move both of them such that right is null
now remove the node

TC: O(n)
Sc: O(n)
"""

def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def deleteNthNode(head):
    dummy = ListNode()
    dummy.next = head
    left = dummy
    right = head

    while n > 0 and head:  # move right by n times
        right = right.next
        n -= 1

    while right:  # move right to end of the list i.e null
        right = right.next  # diff bw left and right is n+1
        left = left.next

    left.next = left.next.next
    # we can not use return head here. imagine input with just 1 node and we want to remove that.
    return dummy.next
