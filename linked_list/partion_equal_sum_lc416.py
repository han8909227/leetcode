
# Given a non-empty array containing only positive integers,
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:
# Input: [1, 5, 11, 5] or  [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.


def partion_subset_sum(data):
    """Return if equal subset exist."""
    total = 0
    for val in data:
        total += val

    if total % 2 == 1:  # if total cannot even divide, no equal subset
        return False

    aim = total / 2  # any combo vals equal to this sum means subset partiion is valid

    boolean_set = set([0])  # keep track of sums
    for val in data:  # loop over arr (get all possible sums)
        for s in boolean_set.copy():  # loop over existing sums
            boolean_set.add(s + val)  # add val to existing sums
    return aim in boolean_set

