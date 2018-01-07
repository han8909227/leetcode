# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.


def binary_search(nums, target):
    """Return index of target val in list nums using binary search."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) / 2  # mid index
        if target == nums[mid]:  # if match target
            return mid  # return index
        if nums[mid] >= nums[left]:  # means left -> mid are in order(not effected by rotation)
            if target < nums[mid] and target >= nums[left]:  # binary search
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < nums[right]:  # means mid -> right are in order(not effected by rotation)
            if target > nums[mid] and target <= nums[right]:  # binary search
                left = mid + 1
            else:
                right = mid - 1
    return -1
