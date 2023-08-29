"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Approach - we use set to store the remaining, we iterate over the nodes and see if it
is already present in set.
actually i didnt' use any BST property here but still it is 98% faster? Confused!!

Tc
Sc
"""

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dic = {}
        curr = root
        while curr:
            remain = k - curr.val
            if remain in dic:
                return True
            dic[curr.val] = 1
            if remain < curr.val:
                curr = curr.left
            if remain > curr.val:
                curr = curr.right
        return False