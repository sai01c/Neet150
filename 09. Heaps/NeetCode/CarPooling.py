"""
https://leetcode.com/problems/car-pooling/

"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = [0] * 1001
        
        for cap, start, end in trips:
            for i in range(start, end):
                points[i] += cap
            
                if points[i] > capacity:
                    return False
                
        return True
            
            