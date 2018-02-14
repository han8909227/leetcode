# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the second array is 3.
#     For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
# Note:
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.


def next_greater(l1, l2):
    """LC 496 implemented in Python."""
    result = []

    for v1 in l1:
        try:
            found = False  # boolean flag
            idx = l2.index(v1)  # find index of val in l2
            temp = l2[idx:]  # cut list from val onword
            while not found:
                for v2 in temp:  # go through partial l2 to find greater val
                    if v2 > v1:
                        result.append(v2)
                        found = True
            continue
        except ValueError:
            result.append(-1)  # append -1 if val not in l2
        result.append(-1)  # append -1 if no greater val
    return result
