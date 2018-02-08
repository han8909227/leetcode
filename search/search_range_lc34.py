# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


def search_range(nums, target):
    """LC34 using binary search."""
    left = 0
    right = len(nums)
    result = []

    while left < right:
        mid = left + right // 2
        if nums[mid] > target:
            right -= 1
        if nums[mid] < target:
            left += 1
        if nums[mid] == target:
