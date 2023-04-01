"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Approach: do bfs then if you get none node while popping, pop the rest of the nodes if any of them is not null return false.

Tc: O(n)
Sc: O(n)
"""

def isCompleteTree(root):
    q = collections.deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node:
            q.append(node.left)
            q.append(node.right)
        else:
            while q:
                if q.popleft():
                    return False
    return True