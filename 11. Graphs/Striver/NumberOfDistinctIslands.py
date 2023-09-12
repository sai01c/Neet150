"""
https://leetcode.com/problems/number-of-distinct-islands/

"""

from collections import defaultdict

def islands(grid):
  rows = len(grid)
  cols = len(grid[0])
  directions = [[0,1],[0,-1],[1,0],[-1,0]]
  cycle = set()
  
  def dfs(r, c, dic, i, j):
    if (r not in range(rows) or
       c not in range(cols) or
       grid[r][c] != 1 or
        (r,c) in cycle):
      return
    cycle.add((r,c))
    dic[i] += 1
    dic[j+100] += 1
    for dr, dc in directions:
      nr, nc = r+dr, c+dc
      dfs(nr, nc, dic, i+dr, j+dc)
  
  distinctIslands = {}
  i = 0
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 1 and (r,c) not in cycle:
        dic = defaultdict(int)
        dfs(r, c, dic, 0, 0) 

        if dic in distinctIslands.values():
          continue
        else:
          distinctIslands[i] = dic
          i += 1

  return len(distinctIslands)