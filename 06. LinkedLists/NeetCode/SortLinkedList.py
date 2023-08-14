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
        dummy = ListNode(0, head)
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        curr2 = head
        i = 0
        nums.sort()
        while curr2 and i < len(nums):
            curr2.val = nums[i]
            i += 1
            curr2 = curr2.next
        return dummy.next