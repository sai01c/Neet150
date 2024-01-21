# Quick Sort
"""
- Pick last element as pivot and check the first element with the pivot if the first element is greater then first element goes to pivot place, pivot moves to the left i.e pivot - 1, this(pivot-1) element goes to the first element place. Total three swap's are done. If the first element is smaller, move on to the next iteration.
- This is done until there no more swaps. Now the pivot element position is fixed. Repeat the same process for left array and right array.
- In-place sorting algorithm
- **_worst case TC O(n ^ 2)_**
- **_average and best case O(nlogn)_**

"""
# write code here
