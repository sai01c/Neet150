"""
https://leetcode.com/problems/permutation-in-string/


Approach: first we iterate through the length of the s1 and 
add count of the s1 string to s1 count array and s2 string to s2 count 
array. Here if the length of s1 is 3 we only take count of the first three
characters of the string s2

now, in s1 count and s2 count - if the string is abde
then [1,1,0,1,1,0,0,....0] length of the count array will be 26. 

Now, as this is a substring problem - we take sliding window concept
and increase the s2count by adding right count and subracting left count
we increase the left pointer every iteration.

if the len of s1 is 3 then we start the right pointer at 3. 
so the substring len is 3 (right - left) 

Tc: O(26n) comparing 26 length arrays
Sc: O(n) arrays

"""


def permutations(s1, s2):
    if len(s1) > len(s2):
        return False

    s1count = [0] * 26
    s2count = [0] * 26

    for i in range(len(s1)):
        index = ord(s1[i]) - ord('a')
        s1count[index] += 1
        index_s2 = ord(s2[i]) - ord('a')
        s2count[index_s2] += 1
    print("s1count", s1count)
    print("s2count:", s2count)

    left = 0
    for right in range(len(s1), len(s2)):
        if s1count == s2count:
            return True

        index_r = ord(s2[right]) - ord('a')
        s2count[index_r] += 1

        index_l = ord(s2[left]) - ord('a')
        s2count[index_l] -= 1
        left += 1

    if s1count == s2count:
        return True

    else:
        return False


print(permutations("ab", "eidbaooo"))
