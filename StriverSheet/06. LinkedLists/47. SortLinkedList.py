# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head

        while curr:
            value = curr.val
            nums.append(value)
            curr = curr.next
        nums.sort()
        
        i = 0
        dummy = ListNode(None)
        prev = dummy
        while i < len(nums):
            first = ListNode(nums[i])
            if i + 1 < len(nums):
                second = ListNode(nums[i+1])
            else:
                second = None
            
            prev.next = first
            first.next = second
            i += 2
            prev = second
        return dummy.next