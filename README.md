# LeetCode Marathon
To aid my coding skill and to succeed in coding interview I am working on a collection of [LeetCode](https://leetcode.com/problemset/all/) problems.

### Goal of this repository
My goal is to help other Python developer who are studying for coding interviews to have a better reference and insight to Leet Code problems, since many of the article/blog on Leet Code problems are written in Java.

### Want to contribute?
* First fork it !
* Add problem and your solution to the appropriate classifier folder
* Submit a pull request to this main repository
* Upon review your contribution will be showing in this repo that will help many others!


## Solved LeetCode Problems

|  #  | Title           |  Solution       | Time  | Space| Notes|
|-----|---------------- | --------------- |-------|------|------|
|200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python](./linked_list/island_count_lc200.py) |_O(m * n)_ | _O(m * n)_|Matrix, LinkedList|
|416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |[Python](./linked_list/partition_equal_sum_lc416.py)|_O(n * s)_ | _O(s)_ ||
|102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)| [Python](./tree/bt_level_order_traversal_lc102.py)|_O(n)_| _O(n)_||
|103 | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)|[Python](./tree/bt_zigzag_traversal_lc103.py)|_O(n)_| _O(n)_||
|98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)|[Python](./tree/verify_tree_is_bst_lc98.py)|_O(n)_| _O(1)_||
|545 | [Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/) | [Python](./tree/bt_boundry_traversal.py)|_O(n)_| _O(h)_||
|236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Python](./tree/bt_lowest_common_ancestory_lc236.py)|_O(n)_| _O(h)_||
|746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | [Python](./dynamic_programming/min_cost_climbing.py)|_O(n)_| _O(1)_||
|33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](./linked_list/search_rotated_array_lc33.py)|_O(logn)_| _O(1)_||
|160| [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)| [Python](./linked_list/intersection_two_ll_lc160.py)|_O(n + m)_| _O(1)_||
|111| [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)| [Python](./tree/bt_min_depth_lc111.py) |_O(n)_| _O(h)_||
|116| [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|[Python](./tree/sibiling_pointer_lc116.py)|_O(n)_| _O(1)_| Asked with LC117|
|117| [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)|[Python](./tree/sibiling_pointer_ii_lc117.py)| _O(n)_ | _O(1)_  |Asked with LC116|
|155| [Min Stack](https://leetcode.com/problems/min-stack/) | [Python](./stack_and_q/min_stack_lc155.py)  | _O(n)_ | _O(1)_ | |
|232| [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) |[Python](./stack_and_q/q_with_stacks_lc232.py) | _O(1), amortized_| _O(n)_| |
|449|[Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/)| [Python](./tree/serialize_and-deserialize_bst_lc449.py)| _O(n)_ | _O(h)_ | |
|547| [Friend Circles](https://leetcode.com/problems/friend-circles/) | [Python](./tree/friend_circles_lc547.py) | _O(n^2)_  | _O(n)_ | Union Find |
|92| [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)| [Python](./linked_list/reverse_linked_list_ii_lc92.py) | _O(n)_| _O(1)_||
|61| [Rotate List](https://leetcode.com/problems/rotate-list/)| [Python](./linked_list/rotated_list_lc61.py)   | _O(n)_ | _O(1)_ | |
|503| [Next Greater Element](https://leetcode.com/problems/next-greater-element-i/description/)| [Python](./linked_list/next_greater_element_lc496.py)| _O(n)_| _O(1)_|Asked with LC503|
|503| [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/description/)| [Python](./linked_list/next_greater_element_ii_lc503.py)| _O(n)_| _O(1)_|Asked with LC496|



## Clarify questions to ask at interview:

1. Array:
    * Sorted or not?
    * How many elements?
    * Element type? Int, float, double?
    * What's the range of those numbers? Positive or negative?
    * Contain duplicates or not?
    * Subsequence: adjacent or not?

2. Binary tree:
    * Binary search tree or normal binary tree?
    * Balanced or not?
    * Complete or not?
    * Has parent pointer or not?

3. Linked list:
    * Singly or doubly linked list?
    * Has duplicated nodal value or not?

4. String:
    * Need to remove white spaces? Tab and newline?
    * Only has digits? English letters? Upper or lower case?

5. Graph:
    * How many nodes and edges?
    * Directed or undirected?
    * Edges have weights? If so, what's the range?
    * Has loops? Negative sum loops?

6. Return value:
    * What should my method return?
    * If there are multiple solutions to the problem, which one should be returned?
    * If it should return multiple values, do you have any preference on what to return?
    * What should I do/return if the input is invalid / does not match the constraints?

## Further problem explaining and solving process:
I have constructed a blog site to post my thought process on solving some of these problems
It can be linked to **[HERE](http://hanblog.tech)**