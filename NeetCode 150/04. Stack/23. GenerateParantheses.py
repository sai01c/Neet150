"""
https://leetcode.com/problems/generate-parentheses/

Approach: this is a backtracking problem. We'll have a base case and list out all the possible cases. 

Revise this problem again with backtracking concept. 
this is Nick white solution. Neetcode used stack with backtracking. 
"""


def generateParenthesis(self, n: int):
    res = []

    def backtrack(output_array, curr_string, openCount, closeCount, maxCount):
        if len(curr_string) == maxCount * 2:
            output_array.append(curr_string)
        if openCount < maxCount:
            backtrack(output_array, curr_string +
                      "(", openCount + 1, closeCount, maxCount)
        if closeCount < openCount:
            backtrack(output_array, curr_string + ")",
                      openCount, closeCount + 1, maxCount)

    backtrack(res, "", 0, 0, n)
    return res


"""
# n = 2 
backtrack(res, "", 0, 0, 2)
0 < 2 => backtrack(output, "(", 1, 0, 2)
            => 1 < 2 => backtrack(output, "((", 2, 0, 2)
            => 0 < 1 => backtrack
                    backtrack(output, "(()", 2, 1, 2)
                        => backtrack(output, "(())", 2, 2, 2)

"""


"""# n = 1 res = ["()"]
backtrack(res, "", 0, 0, 1)

curr_string = ""
open = 0
maxCount = 1
close = 0

0 < 1 = > (output, "(", 1, 0, 1)
        = > (output, "()", 1, 1, 1)
            => len("()") = 2: ["()"]
"""
