"""
https://leetcode.com/problems/reverse-linked-list/

Approach: this is better understood if written on notes.
First, we shift the pointer from current to previous. 
Now, current becomes prev and the actual next (temp) becomes current

this is an iterative approach, recursive watch video again
 
TC O(n) as we are visiting all the nodes once
SC O(n) why TODO

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            temp = curr.next  # storing the variable
            curr.next = prev  # shifting the pointer
            prev = curr #take care about which to assign first prev or curr?
            curr = temp
        return prev


obj = Solution()
head = [2, 3, 4, 5]
print(obj.reverse(head))  # throwing an error
