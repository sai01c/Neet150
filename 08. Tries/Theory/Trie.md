## Trie

- Trie is also called as prefix tree.
- Trie is a data structure that looks like a tree but it stores charactar's as node.
- The path of nodes together form a word.
- Trie (we pronounce "try") or prefix tree is a tree data structure, which is used for retrieval of a key in a dataset of strings.
- There are various applications of this very efficient data structure such as :
Autocomplete, spellchecker, IP routing, predictive text, word games. 

- Tc: O(len(string)) for search, insert, delete

- Although hash table has O(1)O(1) time complexity for looking for a key, it is not efficient in the following operations :

Finding all keys with a common prefix.
Enumerating a dataset of strings in lexicographical order.

- Another reason why trie outperforms hash table, is that as hash table increases in size, there are lots of hash collisions and the search time complexity could deteriorate to 
O(n),  where n is the number of keys inserted. 
- Trie could use less space compared to Hash Table when storing many keys with the same prefix. 
- In this case using trie has only O(m) time complexity, where m is the key length. 
- Searching for a key in a balanced tree costs O(mlogn) time complexity.