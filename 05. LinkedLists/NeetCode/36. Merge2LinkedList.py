"""
https://leetcode.com/problems/merge-two-sorted-lists/

Approach: this is merge sort algorithm. 
First, we compare the l1 and l2 value and append it to the dummy node. 
Now, if any of the l1 or l2 are remaining we append the pointer to them. 

Tc: O(m+n) as we are just merging here
Sc: O(1) 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge2linkedlists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val: #attach based on value
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next #always shift the tail pointer

    if l1:  # if any l1 is remaining, attach the pointer to the rest of the l1
        tail.next = l1
    else:  # poiner to the rest of the l2.
        tail.next = l2
    return dummy.next  # tail is the pointer, dummy is the empty node.
