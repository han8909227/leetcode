# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.


def jump(nums):
    """
    3 situations,
    1: you get to the end exactly
    2: end is within your reach
    3: you are not at end and hit a zero and will not get any further.
    """
    idx = 0
    while True:
        idx += nums[idx]
        if idx >= len(nums):
            return True
        if nums[idx] == 0:
            return False
