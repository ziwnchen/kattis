# MPCS 51100 PSet 2
## Starting Framework

Include any notes on your implementation 
as well as your results for problem 6
in this file.

- Student Name: Ziwen Chen
- Student Email: ziwenchen@uchicago.edu	

### Problem 1 and 2:
Description: Use recursive and non-recursive method to examine if a binary tree is BST or not
Reference: [check bst](https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/)

### Problem 4:
Description: Build BST to store dictionary.
Potential problems: 
- **String format of definition:** when the user manually adds a word to the dictionary, all characters related to the word definition will be kept, including the double quotation mark. I think this is more convenient for users who might feel unconformable to add the double quotation mark every time. 
- **Format of printing:** no specific printing format requirement has been found in the assignment. The format of printing might be different compared to standard solution.
- **Memory leakage**: there might be memory leak when creating the tree node.

### Problem 5:
Description: Use Red Black tree to re-implement Problem 4.
Potential problems: 
- **Memory leakage**: there might be memory leak when creating the tree node.
Reference: [Red Black Tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)

### Problem 6 Results:
Naive BST Dictionary
- Time to import (sec): 2.86004 (s)
- Avg. time per find (us): 33.69992(us)

Self Balancing BST Dictionary
- Time to import (sec): 0.10784 (s)
- Avg. time per find (us): 2.69102(us)

### Discussion:
The above outcome indicates that Self-Balancing BST is faster than Naive BST both in adding large numbers of nodes and in node searching. This is not surprsing because Self-Balancing BST has lower tree height. Although it may take some extra time to rotate the tree and reorder the nodes, Self-Balancing BST is still much better in importing large data with alphabetical order. As for node searching, in the current example (alphabetised dictionary), the time complexity of a Naive BST is O(n) while the time complexity of a Self-Balancing BST is O(log n).

### Problem 7:
Description: Use multiple binary searches for each given array.
Reference: [Binary Search](https://en.wikipedia.org/wiki/Binary_search_algorithm)

### Problem 8:
Description: I improved the binary search I used in Problem 7 to interpolation search. 
- **Search Time Complexity**: On average the time complexity of interpolation search is about log(log(n)) (if the data in the array are uniformly distributed), where n is the length of array to be searched. In the worst case, the time complexity can be up to O(n).
- **Memory Usage Requirement**: The data structure of grid is not changed. The memory space of a grid is the size of arrays plus grid characteristics(size, array length).
Potential problems: Interpolation search is only faster than binary under the condition that the data in the array are uniformly distributed. Therefore, only to cetain kind of array can this method be useful. Have to admit, interpolation search is not an ideal solution to Problem 8. 

Reference: [Interpolation search](https://en.wikipedia.org/wiki/Interpolation_search)