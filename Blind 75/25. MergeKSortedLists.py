"""
https://leetcode.com/problems/merge-k-sorted-lists/

Approach: first we need to use the merge 2 lists method.
break down the initial lists into 2 each and apply merge2lists method
now add the merged list into a new list and continue until length of the newly list is only 1

this is linked list solution. Not sure how to do using heaps?
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
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None
            mergedLists.append(merge2lists(l1, l2))
        lists = mergedLists
    return lists[0]
