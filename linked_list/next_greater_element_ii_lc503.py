# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.


def next_greater_ii(nums):
    """LC 503 implemented in Python."""
    nums_len = len(nums)  # actual len of list
    result = [-1 for n in range(nums_len)]  # result list
    for i in range(nums_len):
        j = i + 1  # starting next val
        while j < i + nums_len:  # while less than 1 iteration. i.e 2(curr), 3, 4(tail), 5, 6
            if nums[j % nums_len] > nums[i]:  # ensure in range
                result[i] = (nums[j % nums_len])
                break
            j += 1
    return result
