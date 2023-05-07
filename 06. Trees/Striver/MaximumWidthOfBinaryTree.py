"""
https://leetcode.com/problems/maximum-width-of-binary-tree/

Approach 

tc
sc

"""

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((0, root))
        ans = 0
        while q:
            minheap, maxheap = [], []
            for i in range(len(q)):
                ind, node = q.popleft()
                
                heapq.heappush(minheap, ind)
                heapq.heappush(maxheap, -ind)
                
                if node.left:
                    q.append((2*ind+1, node.left))
                if node.right:
                    q.append((2*ind+2, node.right))

            mini = minheap[0]
            maxi = maxheap[0] * -1
            ans = max(ans, maxi - mini + 1)
        return ans
