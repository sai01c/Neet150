"""
https://leetcode.com/problems/mice-and-cheese/

tc - nlogn
sc - n
"""

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        visit = set()
        heap = []
        res = 0
        
        if k == len(reward1): #this means we only need rewards1 elements
            for r in reward1:
                res += r
            return res
        
        for i in range(len(reward1)): #add diff of 1-2 to heap
            diff = reward1[i] - reward2[i]
            heapq.heappush(heap, (-diff, reward1[i], i))
        
        #take the maximum difference available from rewards1
        while heap and k > 0: #add only k elements from rewards1
            diff, val, ind = heapq.heappop(heap)
            visit.add(ind) #mark this index visited
            res += (val) #add to our res
            k -= 1 #decrease k by -1

        for i in range(len(reward2)): #add left over elements if they are not visited
            if i not in visit:
                res += reward2[i]
        
        return res
            
            
            
           
                
        
        