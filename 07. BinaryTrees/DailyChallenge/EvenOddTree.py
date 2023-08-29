"""
https://leetcode.com/problems/even-odd-tree/

"""

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append(root)
        even = True
        while q:
            if even: prev = float('-inf')
            if not even: prev = float('inf')
   
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    curr = node.val
                    if even:
                        if curr % 2 == 0 or curr <= prev:
                            return False
                    else:
                        if curr % 2 != 0 or curr >= prev:
                            return False
                    prev = curr   
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            even = not even
        
        return True
                    
        