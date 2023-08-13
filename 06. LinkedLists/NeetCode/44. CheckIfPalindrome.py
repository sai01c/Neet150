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
        dummy = ListNode()
        dummy.next = head
        first = head
        #go to middle using slow and fast pointers
        slow = dummy
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        #reverse the second half now
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev
        
        #now compare first and second lists if they are equal
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
        