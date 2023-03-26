"""
https://leetcode.com/problems/balanced-binary-tree/

Tc: O(n^2)
"""

class Solution:
    def isBalanced(self, root) -> bool:
        if not root:  # if there is no node that means our balance condition is not failing
            return True  # so we return true here
        l = self.height(root.left) #calculate height
        r = self.height(root.right)
        if (abs(l - r)) > 1: 
            return False
        left = self.isBalanced(root.left) #call function on its children as well
        right = self.isBalanced(root.right)
        if (not left) or (not right): #if either of them is failing entire tree fails
            return False
        return True #if everything is passing 

    def height(self, root): #generic height function
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
Sc: O(n) recursive call stack
"""

class Solution:
    def isBalanced(self, root) -> bool:
        return self.height(root) != -1 #if -1 then imbalanced

    def height(self, root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        if lh == -1 or rh == -1: #if any of the node is imbalanced then it is failing
            return -1
        if abs(lh - rh) > 1: #if they are imbalanced return height as -1
            return -1
        return 1 + max(lh, rh) #return height as usual
