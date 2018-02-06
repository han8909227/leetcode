"""Simple binary search."""


def bs(nums, target):
    """."""
    left = 0
    right = len(nums)
    while left < right:  # two pointers can merge, not cross
        mid = (left + right) // 2  # only search for mid index
        # import pdb; pdb.set_trace()
        if nums[mid] > target:  # push mid idx to left
            right -= 1
        if nums[mid] < target:  # push mid idx to right
            left += 1
        if nums[mid] == target:
            return mid
    return -1  # val not exist

