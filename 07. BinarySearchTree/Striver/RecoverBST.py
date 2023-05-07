"""
https://leetcode.com/problems/recover-binary-search-tree/

Approach - we first get the inorder traversal of given tree and then sort it. Now, 
this sorted one is the correct inorder traversal. using this one we will modify the 
original one.

Tc
sc
"""

def func(root):
    if not root:
        return
    nums = []
    correct = []
    def inorder(root): #inorder traversal
        if not root:
            return 
        inorder(root.left)
        nums.append(root) #we are appending entire node
        inorder(root.right)

    inorder(root)
    for node in nums:
        correct.append(node.val)
    correct.sort() #this gives the correct order

    for i in range(len(nums)):
        nums[i].val = correct[i]
