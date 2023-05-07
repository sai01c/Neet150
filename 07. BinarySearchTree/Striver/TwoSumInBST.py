"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Approach - we use set to store the remaining, we iterate over the nodes and see if it
is already present in set.
actually i didnt' use any BST property here but still it is 98% faster? Confused!!

Tc
Sc
"""

def func(root, k):
    visit = set()
    def helper(root):
        if not root:
            return
        if root.val in visit:
            return True
        remain = k - root.val
        visit.add(remain)

        if helper(root.left):
            return True
        
        if helper(root.right):
            return True
        
        return False