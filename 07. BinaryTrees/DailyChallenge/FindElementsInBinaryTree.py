"""
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

"""
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.visit = set()
        self.root = self.bfs(self.root, self.visit)
        
    def bfs(self, root, visit):
        q = collections.deque()
        q.append((root, 0))
        while q:
            for i in range(len(q)):
                node, ind = q.popleft()
                if node:
                    node.val = ind
                    visit.add(ind)
                    if node.left:
                        q.append((node.left, 2*ind+1))
                    if node.right:
                        q.append((node.right, 2*ind+2))
        return root
        

    def find(self, target: int) -> bool:
        if target in self.visit:
            return True
        return False