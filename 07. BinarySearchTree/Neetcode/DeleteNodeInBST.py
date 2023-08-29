"""
https://leetcode.com/problems/delete-node-in-a-bst/

Approach - iterate using BST property and after you found the node.
you need to replace this node visit right subtree and go as left as possible. Now, place
this node val in the given key place

TODO

tc
sc
"""

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        if key < root.val:
            #do recursive function on left
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            #do recursive function on right
            root.right = self.deleteNode(root.right, key)
        else:
            #only right is there so we can return right
            if not root.left:
                return root.right
            #only left is there so we can return left
            elif not root.right:
                return root.left
            #if both left and right are there so, we find the leftest possible among 
            #the right subtree and now replace that value to the original key value 
            #and continue to do the recursive function on right subtree and the value will 
            #change to root.val (the one you replaced with)
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root
