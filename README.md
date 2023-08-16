# Takeaways

- Counter is basically a dictionary. In python, dictionary doesn't store the order. So, if you want to sort them copy to a list while sorting it. `sortedCount = sorted(dict.items(), key = lambda x: x[1], reverse = True)`
- If the problem is about frequency/ count, use dictionary.
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
- Sliding window - have two pointers left and right. Iterate the array using right. Change left based on condition. Used for substring problems, buy and sell stock problems.
- Set- remove TC O(1)
- Whenever we have frequency, we need to use dictionary to store the frequency of elements/char.
- Anagram: Use dictionary to store counts/ frequencies. 
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
- `index = ord(s1[i]) - ord('a')` gives the index of the alphabets. Eg- a is 0, b is 1, c is 2, d is 3, z is 25. 
- deque inserting deleting the element is O(1)
- Use stacks when you want to compare one element with other element. Adding and deleting is also O(1) we can use for this reason
- Use heaps if you want the largest/smallest element.
- For BST, always think of sorting approaches. They are very similar to Binary Search.
- For BST, if you do inorder traversal, we get sorted array. 
- To get Random element from a list - random.choice(array)
- Instead of creating a frequency dictionary and sorting it, see if you can create an
array and use index as frequency. This will eliminate sorting the frequency. Eg: if it is frequency of alphabets, you can create an array with index a, b, c, d until z. Eg: Top K frequent elements.
- Sorted array - always try two pointer approach.
- For undirected graph, always add both edges s -> e and e -> s to our adjacency list.
- If we want to find the maximum or minimum from an array always use heaps.
- In python, by default, we will have min heap. We can convert this to max heap by multiplying all the elements by -1 and we can use abs(value) in the end to return the original value.
- If we want to find the kth largest element in an array using heap, other approach is to continue usin the default min-heap in python. But, we pop the min-heap until we have k elements in an array.
  `Eg: input= [1,2,3,,4,5] k = 3 we pop 2 times i.e 1,2 will be removed. input = [3,4,5] It has k number of elements. If we pop now we get the head which is the kth largest element in the orginal input.`
- Counter(nums)- dict with keys as elements in nums and values as the frequency of those elements in nums.
- nums = [1,1,2,2,2,3,4] `count = Counter(nums) = {1:2, 2:3, 3:1, 4:1}`
- Counter by default sorts the items by highest frequency. But, while iterating over a counter it will iterate based on the order of the elements in the original input not by the frequency. So, always copy a counter to new list and iterate over the list to get the sorted frequency. To summarize, dictionary in python doesn't store the order so always copy the dict to new list while sorting it.
- sortedList = `sorted(dict.items(), key= lambda x:x[1], reverse= True)` sorts the dictionary by values i.e. frequency. `[{2:3, 1:2, 3:1, 4:1}]`
- If we want to add elements or remove the last element, we may want to use stack there. For its pop operation(LIFO)
- For Binay Search, if the input is not sorted but the intended output has lower and upper intervals then you can use binary search because output will be a sorted array b/w those intervals.
- For sorting an array, you can eliminate sorting in n logn by using indexes of array as sorting. Eg: you need to sort array based on frequency. You can create a frequency array where the index represents the frequency and this way you can sort in just O(n)
- Two heaps pattern - IPO, Median of Data Stream.
- If you want to go to the middle of linked list, use slow and fast pointer technique.
- In linked list, if you assign one pointer to head and shift that pointer. You can still go back to head by using another pointer. But, if you change the node.next using the first pointer it will remain same with second pointer as well.
- To remove key, value from dic - dic[key].remove(value)
- Use BFS if you want to calculate time, cost etc because in BFS we can add for loop and calculate all nodes at once. Eg - Rotten oranges, wall gates, word ladder etc.
- To get negation of 0, 1 peform XOR operation with 1. 0 ^ 1 is 1 and 1 ^ 1 is 0
- Use Zip function to compare two strings. Eg: a = 'sai' b = 'sha' for i, j in zip(a,b) gives i j values as a s, a h, i a
- In dic, we can only have immutable data type as keys - int , string , tuple
- If we want to remove adjacent elements always consider stack first
- If paranthesis problems, always do stack first
- In sliding window, to reduce from n**2 to n use dict, set or queue. 
- Constructor for Doubly linked list - 
```
class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
```