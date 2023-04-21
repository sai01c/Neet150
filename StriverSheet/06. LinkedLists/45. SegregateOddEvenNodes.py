# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy2 = ListNode(0)
        first = head
        second = first.next
        dummy.next = first
        dummy2.next = second
        
        while first and first.next and second and second.next:
            temp2 = second.next.next
            temp = first.next.next
            
            first.next = temp
            second.next = temp2
            
            first = first.next
            second = second.next
            

        first.next = dummy2.next
        return dummy.next

        