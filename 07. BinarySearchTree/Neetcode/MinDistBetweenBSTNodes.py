"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/

Approach: this is a Binary Search Tree. left subtree < root < right subtree
we do inorder traversal ( left root right) this will give sorted array
do sliding window to find the diff b/w two adjacent elements and get the min among them. 

TC: O(n)
Sc: O(n)
"""

def minDist(node):
    res = []
    inOrder(node, res)
    left = 0
    ans = float("inf")
    for right in range(len(res)):
        diff = res[right] - res[left]
        ans = min(diff, ans)
        left += 1
    return ans

def inOrder(root, res):
    if not root:
        return None
    inOrder(root.left, res)
    res.append(root.val)
    inOrder(root.right, res)

    return res
