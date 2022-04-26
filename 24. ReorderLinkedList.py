"""
https://leetcode.com/problems/reorder-list/

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Approach: divide the linked list into two halves.
use two pointer slow and fast to find out the mid 
First half should be normal and second should be reversed. 
merge both the halves. 
"""

#example [1,2,3,4,5]


def reOrder(head):
    slow = head
    fast = head.next
    # to find out the mid of the linkedlist
    while fast and fast.next:  # as we are incrementing fast pointer by 2 we should check for fast.next also
        slow = slow.next
        fast = fast.next.next
    # slow at 3, fast at None

    # reverse the linked list- [4,5]
    current = slow.next
    slow.next = None  # closing the first half of the linkedlist
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    #now [5,4]

    # merging the revered second half and first half
    first = head  # 1
    second = prev  # 5
    while second:
        t1 = first.next
        t2 = second.next
        first.next = second
        second.next = t1
        first = t1
        second = t2
