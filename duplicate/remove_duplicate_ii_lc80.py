# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.


def remove_duplicate(nums):
    """LC 80."""
    set_a = set()
    set_b = set()  # two sets, if entered second set means we have 3 or more repeating
    n = len(nums)

    for i in range(n - 1):
        if nums[i] in set_b:
            if i == n - 1:
                nums = nums[:i]
            else:
                nums = nums[:i] + nums[(i + 1):]
        elif nums[i] in set_a:
            set_b.add(nums[i])
        else:
            set_a.add(nums[i])
    return nums


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
