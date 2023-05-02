"""
https://leetcode.com/problems/rank-teams-by-votes/

Approach - this is very famous question for Atlassian
First for every character we need to create an array with 0
This array represents the number of votes they got for 0th index, 1st index etc
So length of the array will be length of the word
length of the dic will also be length of the word
Then we need to sort based on the descending order of the arrays
if two arrays are same then we choose the smallest alphabet

{
    'A': [5, 0, 0], 
    'B': [0, 2, 3], 
    'C': [0, 3, 2]
}

Tc - n^2
Sc - n

"""


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        dic = {}

        for char in votes[0]: #create an array for every character
            dic[char] = [0] * len(votes[0])
        
        
        for word in votes: #increment count by 1 for every character, position
            for ind, char in enumerate(word):
                dic[char][ind] += 1
        
        res = ""
        #sort based on arrays
        #if two arrays are same then we choose the smallest alphabet so we multiplied by -1
        sortList = sorted(dic.items(), key = lambda x:(x[1], -ord(x[0])), reverse = True)
        for k, v in sortList:
            res += k
            
        return res

