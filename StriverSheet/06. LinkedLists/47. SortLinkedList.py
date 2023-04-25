"""
https://leetcode.com/problems/sort-list/

approach - first sort the linked list by copying values to an array
after sorting the array, use two pointers to create linked list and join them

tc - nlogn
sc - n
"""

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
            #create first and second nodes, check if second is in bounce
            first = ListNode(nums[i])
            if i + 1 < len(nums):
                second = ListNode(nums[i+1])
            else:
                second = None
            #join the nodes
            prev.next = first
            first.next = second
            #increase the pointer and update prev node
            i += 2
            prev = second
        
        return dummy.next