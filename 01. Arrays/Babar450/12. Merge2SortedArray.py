"""

https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1

"""

# Input:
N = 4,
M = 5
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
# Output: 0 1 2 3 5 6 7 8 9


i = j = k = 0
new = [0] * 9
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        new[k] = arr1[i]
        i += 1
        k += 1
    else:
        new[k] = arr2[j]
        j += 1
        k += 1
while i < len(arr1):
    new[k] = arr1[i]
    i += 1
    k += 1

while j < len(arr2):
    new[k] = arr2[j]
    j += 1
    k += 1
print(new)

# With out using extra space-
