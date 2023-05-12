"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Approach: mid of the array will be root of binary tree
left and right will be recursive calls

"""

def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root
