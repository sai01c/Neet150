"""
https://leetcode.com/problems/balanced-binary-tree/

Brute force approach: 
I'll have a height function and find the height at every left and right
if the difference is more than 1 return False
repeat the function for every left and right node

Tc: O(n^2)
"""


class Solution:
    def isBalanced(self, root) -> bool:
        if not root:  # if there is no node that means our balance condition is not failing
            return True  # so we return true here
        l = self.height(root.left)
        r = self.height(root.right)
        if (abs(l - r)) > 1:
            return False
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        if (not left) or (not right):
            return False
        return True

    def height(self, root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return 1 + max(lh, rh)


"""
Optimal approach: 
have a function for height and check the balance condition there itself
if the diff bw left and right > 1 then return -1

Tc: O(n)
Sc: O(n) auxillary space
"""


class Solution:
    def isBalanced(self, root) -> bool:
        return self.height(root) != -1

    def height(self, root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        if lh == -1 or rh == -1:  # add the conditions here itself
            return -1
        if abs(lh - rh) > 1:  # this will reduce the tc to O(n)
            return -1
        return 1 + max(lh, rh)
