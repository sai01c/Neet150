"""
https://leetcode.com/problems/dota2-senate/

Approach - 

tc - n
sc
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = collections.deque()
        dq = collections.deque()
        n = len(senate)
        
        #add indexes to the two queue's for R and D
        for i, char in enumerate(senate):
            if char == "R":
                rq.append(i)
            else:
                dq.append(i)
        
        #pop from left and append back the least index
        while rq and dq:
            rchar = rq.popleft()
            dchar = dq.popleft()
            
            #we are adding n because we can go circular direction and next iteration
            #highest index can capture least index to compensate this we are adding length
            #we want to add the length for this reason

            #remember for circular array how adding array two times will solve this is also same

            if rchar < dchar:
                rq.append(rchar + n)
            else:
                dq.append(dchar + n)
                
        if rq:
            return "Radiant"
        if dq:
            return "Dire"