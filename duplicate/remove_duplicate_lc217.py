# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


def remove_duplicate(nums):
    """LC 217."""
    seemed = set()

    for val in nums:
        if val not in seemed:
            seemed.add(val)
        else:
            return True
    return False


if __name__ == "__main__":

    f = [n for n in range(10)]
    t = f + [n for n in range(5)]
