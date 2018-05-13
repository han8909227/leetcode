# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.


def jump(nums):
    """Classic greedy algo."""
    idx = 0
    longest = 1
    length = len(nums)

    while idx <= longest:  # potential jump
        if longest >= length - 1:  # means reached or excceding last idx
            return True
        longest = max(longest, idx + nums[idx])  # greedy part, if you can bring me further
        idx += 1
    return False
