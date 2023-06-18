"""
https://leetcode.com/problems/unique-paths-ii/
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[rows-1][cols-1] == 1:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        #changing blocker to -1
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1
        
        obstacleGrid[rows-1][cols-1] = 1
        #put 1 in boundaries if no blocker
        for r in range(rows-2, -1, -1):
            if obstacleGrid[r+1][cols-1] != -1:
                obstacleGrid[r][cols-1] += obstacleGrid[r+1][cols-1]
            else:
                obstacleGrid[r+1][cols-1] = 0
                
        for c in range(cols-2, -1, -1):
            if obstacleGrid[rows-1][c+1] != -1:
                obstacleGrid[rows-1][c] += obstacleGrid[rows-1][c+1]
            else:
                obstacleGrid[rows-1][c+1] = 0
        
        #calculate from bottom
        for r in range(rows-2, -1, -1):
            for c in range(cols-2, -1, -1):
                if obstacleGrid[r][c] == -1:
                    continue
                else:
                    if (obstacleGrid[r+1][c] != -1 and obstacleGrid[r][c+1] != -1):  
                        obstacleGrid[r][c] = (obstacleGrid[r+1][c] + obstacleGrid[r][c+1])
                    elif obstacleGrid[r+1][c] == -1:
                        obstacleGrid[r][c] = obstacleGrid[r][c+1]
                    elif obstacleGrid[r][c+1] == -1:
                        obstacleGrid[r][c] = obstacleGrid[r+1][c]
                    else:
                        obstacleGrid[r][c] = 0
        
        if obstacleGrid[0][0] != -1:
            return obstacleGrid[0][0]
        else:
            return 0
                