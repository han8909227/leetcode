# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.


def remove_duplicate(nums):
    """LC26."""
    seemed = set()
    idx = 0
    while idx < len(nums):
        if nums[idx] in seemed:
            nums = nums[:idx] + nums[(idx + 1):]  # remove the duplicating val
        else:
            seemed.add(nums[idx])
            idx += 1  # only progress if new val, otherwise we'll be skipping vals
    return nums


if __name__ == '__main__':
    test_list = sorted([num for num in range(10)] + [num for num in range(10)])
