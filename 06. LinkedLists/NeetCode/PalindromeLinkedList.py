"""
https://leetcode.com/problems/palindrome-linked-list/

Approach - go to the middle of the linked list using slow and fast pointers.
then reverse the second half now iterate over the first and second lists and compare them to 
see if they are equal

tc - n
sc - 1

"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first = head
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True