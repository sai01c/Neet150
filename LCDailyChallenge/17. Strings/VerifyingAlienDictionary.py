"""
https://leetcode.com/problems/verifying-an-alien-dictionary/

Approach - take the min length and compare two words

tc - length of words * max length of word
sc - 1

"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            
            mini = min(len(w1), len(w2))
            j = 0

            while j < mini:
                c1 = w1[j]
                c2 = w2[j]
                if c1 != c2:
                    #if they are diff compare first character
                    # first should be lesser than second
                    if order.index(c1) > order.index(c2):
                        return False
                    else:
                    #this iteration satisfied proceed to next set of words
                    #because we are just comparing first character in each word
                        break
                else:
                    j += 1
                    #bigger length should come second if they have common prefix
                    if j == mini and len(w1) > len(w2): 
                        return False
                    
                
        return True