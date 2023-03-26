"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

APPROACH: solution available on LC. 
we inorder traversal and get the elements in ascending order then find the kth element

Tc: O(n) traverse every node once
Sc: O(n) using array here
"""


def kthSmall(root):
    return inorder(root)[k-1]


def inorder(root):
    if not root:
        return []  # since we are trying to return array with elements
    return inorder[root.left] + [root.val] + inorder[root.right]
    # + here basically adds the elements to a single array


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
