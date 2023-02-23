"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

APPROACH: we do inorder traversal and get the elements in ascending order
then find the kth element. Inorder traversal of BST gives sorted array

Tc: O(n) traverse every node once
Sc: O(n) using array here
"""


def kthSmall(root):
    self.res = []
    inorder(root)
    return res[k-1]


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    self.res.append(root.val)
    inorder(root.right)

    return self.res

"""
we can also use iterative inorder using stack 

Tc: O(n) traverse every node once
Sc: O(n) stack
"""

def kthsmalll(root):
    stack = []
    curr = root
    while stack and curr:
        while curr:
            stack.append(curr)
            curr = curr.left  # add the left possible element to the stack
        curr = stack.pop()  # this will give the top most element which should be the least
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right
