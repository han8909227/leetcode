# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# Note:
# You can assume that you can always reach the last index.


def jump_game_ii(nums):
    """Min step to complete the jump game."""
    length = len(nums)
    counter = 0
    longest = 0
    reach = 0

    for i in range(length):
        if longest < i:  # if i is ahead of longest (curr longest cannot complete game)
            counter += 1  # need to jump
            longest = reach  # update the longest
        reach = max(reach, nums[i] + i)  # determine what reach is for this i, either previous reach or curr val + idx
    return counter
