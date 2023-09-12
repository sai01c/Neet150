"""
topView - not there in leetcode
"""

def bottomView(root):
  if not root: return []
  q = collections.deque()
  q.append((root, 0)) #(node, horizontal distance)
  while q:
    for i in range(len(q)):
      node, dist = q.popleft()
      if node:
        dic[dist].append(node)
        q.append((node.left, dist-1))
        q.append((node.right, dist+1))
  res = []
  for dist, nodes in dic.items():
    res.append(nodes[-1])
  return res
