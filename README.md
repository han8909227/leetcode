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



## Clarify questions to ask at interview:

1. Array:
(1) Sorted or not?
(2) How many elements?
(3) Element type? Int, float, double?
(4) What's the range of those numbers? Positive or negative?
(5) Contain duplicates or not?
(6) Subsequence: adjacent or not?

2. Binary tree:
(1) Binary search tree or normal binary tree?
(2) Balanced or not?
(3) Complete or not?
(4) Has parent pointer or not?

3. Linked list:
(1) Singly or doubly linked list?
(2) Has duplicated nodal value or not?

4. String:
(1) Need to remove white spaces? Tab and newline?
(2) Only has digits? English letters? Upper or lower case?

5. Graph:
(1) How many nodes and edges?
(2) Directed or undirected?
(3) Edges have weights? If so, what's the range?
(4) Has loops? Negative sum loops?

6. Return value:
(1) What should my method return?
(2) If there are multiple solutions to the problem, which one should be returned?
(3) If it should return multiple values, do you have any preference on what to return?
(4) What should I do/return if the input is invalid / does not match the constraints?
