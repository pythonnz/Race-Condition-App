# Merge Two Sorted Lists

You are given two sorted lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the values of the first two lists.

Return merged list. **You may not use `sorted()` or `heapq.merged()`**

Example 1

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1, 1, 2, 3, 4, 4]
```

Example 2:

```
Input: list1 = [], list2 = []
Output: []
```

Example 3:

```
Input: list1 = [], list2 = [0]
Output: [0]
```

Constraints:

 * The number of entries in both lists is in the range `[0, 50]`.
 * The values of each item in the list are between `-100` and `100`
 * Both `list1` and `list2` are sorted in non-decreasing order.
