"""
https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        q = collections.deque()
        q.append(root)
        dic = defaultdict(list)
        visit = set()
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        dic[node.left.val].append(node.val)
                        dic[node.val].append(node.left.val)
                    if node.right:
                        dic[node.right.val].append(node.val)
                        dic[node.val].append(node.right.val)
        
        for node in dic:
            if node == k:
                q.append(k)
                visit.add(k)
        
        while q:
            node = q.popleft()
            if len(dic[node]) <= 1:
                return node
            for nei in dic[node]:
                if nei not in visit:
                    q.append(nei)
                    visit.add(nei)