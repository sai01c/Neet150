"""
https://leetcode.com/problems/merge-k-sorted-lists/

Approach: we use the merge 2 lists method 
each iteration we take two lists and append it as 1 to the original lists. 
repeat until the original lists just has one list

TC: O(n^2) TODO
SC: O(n)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKlists(lists):
    if len(lists) == 0:
        return None
    while len(lists) > 1:  # repeat until it has only 1 list.
        mergedLists = []
        for i in range(0, len(lists), 2):  # take two lists at a time. eg 0,1 and then 2,3
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None
            # we merge the two lists into one and append it.
            mergedLists.append(merge2lists(l1, l2))
        # update the lists after the for loop is completed as we need to check the while condition.
        lists = mergedLists
    return lists[0] #0th index has the linked list so just return that. 



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
