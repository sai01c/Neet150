# Takeaways from Blind 75

- Counter is basically a dictionary. In python, dictionary doesn't store the order. So, if you want to sort them copy to a list while sorting it. `sortedCount = sorted(dict.items(), key = lambda x: x[1], reverse = True)`
- If the problem is about frequency, use dictionary.
- If the problem is about duplicate, use set.
- Sorted input - binary search
- For while loop, always make the computation inside the while loop.

  ```
  while left<right:
    mid = (left+right)//2
  ```

- For matrices, we always need to use two for loops

```
m = len(matrix) #number of rows
n = len(matrix[0]) #number of columns
for r in range(m):
  for c in range(n):
    matrix[r][c] #gives the element
```

- For matrices, common approach is to have 4 pointer's- left, right, top, bottom
- For matrices, when making operations always visulaize row and column and make the changes.
- comment down the co-ordinates for easy visualization
- For intervals, most of the cases we sort them. 
- Easier to use `for start, end in intervals` while iterating over them. 
- For linked lists, `current.next = previous`. Pointer/direction from current node to previous node.
- `temp = current.next` temp stores the node next to current node. 
- `slow = slow.next` you are shifting the pointer by one node. 
- `fast = fast.next.next` you are shifting the pointer by two nodes. 
- adding or removing elements to the heap O(logn)
- finding max or min in a heap O(1)
- if you are looking for uniques, always use set. 
- Substring problems - sliding window technique. `left, right = 0, for i in range(len(nums))`
- Set- remove TC O(1)
- Whenever we have frequency, we need to use dictionary to store the frequency of elements/char.
- `count[element] = count.get(element, 0) + 1`
- If we want a palindrome, always use two pointers left and right
- For palindromic substring, always use helper function to calculate from the mid. 
```
def palindromicSubstring(s, left, right):
  while left >= 0 and right < len(s) and s[left] == s[right]:
    left -= 1
    right += 1
```
- If nums is the input array, we can directly create a set using set(nums). Again, set is used when we need to find the unique elements. Time complexity for this operations is O(n) as we need to iterate over nums to create set.
- `collections.deafultdict(set)` this is a dictionary with set functionality. key is unique. values can be more than one. Example: defaultdict(<class 'set'>, {0: {'5', '7', '3'}, 1: {'5', '9', '1', '6'}, 2: {'9', '8', '6'}}).
- To sort a string. input "eat". `sortedString = "".join(sorted(input))` sortedString = "aet"
- Whenever, we have array in two dimensional graph - we use two pointers and increase/decrease the pointers. Eg. Container with most water, trapper rain water. 
- sliding window - have two pointers left and right. Iterate the array using right. Change left based on condition. Used for substring problems, buy and sell stock problems. 
- `index = ord(s1[i]) - ord('a')` gives the index of the alphabets. Eg- a is 0, b is 1, c is 2, d is 3, z is 25. 
- deque inserting deleting the element is O(1)