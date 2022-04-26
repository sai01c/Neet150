"""
https://leetcode.com/problems/merge-k-sorted-lists/

lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Approach: first we need to use the merge 2 lists method.
break down the initial lists into 2 each and apply merge2lists method
now add the merged list into a new list and continue until length of the newly list is only 1
"""


def merge2lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


def mergeKlists(lists):
    if len(lists) == 0:
        return None
