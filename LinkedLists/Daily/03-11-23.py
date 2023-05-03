"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Approach: this is similar to sorted array to linked list
we find the middle and root will be this value
elements before middle will be root.left
elements after middle witll be root.right

base condition - if we don't get linkedlist we return None
also if element.next is None we return TreeNode(element.val)

Tc: 
Sc: 
"""

def sortedListToBST(head):
    if not head: return None
    if not head.next: return TreeNode(head.val) #this is another condition to avoid repeatition
    dummy = ListNode()
    dummy.next = head
    slow = dummy
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    middle = slow.next
    second = middle.next
    middle.next = None
    slow.next = None
    first = head

    root = TreeNode(middle.val)
    root.left = sortedListToBST(first)
    root.right = sortedListToBST(second)

    return root

dic = {1: 1}
print(max(dic.values()))