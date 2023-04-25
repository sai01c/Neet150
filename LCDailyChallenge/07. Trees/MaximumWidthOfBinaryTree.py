"""
https://leetcode.com/problems/maximum-width-of-binary-tree/

Approach - while inserting use index. its children will be 2*ind+1 and 2*ind+2
this is the property of binary tree use this to calculate how many nodes we will have in total
use min heap and max heap to get the min and max of each level and maintain res to get the max
of all levels

tc - nlogn
sc - n

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