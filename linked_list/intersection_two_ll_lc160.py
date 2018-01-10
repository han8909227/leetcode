# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.


class LinkedList(object):
    """Simple linked list class."""

    def __init__(self, val):
        """."""
        self.next = None
        self.val = val


def intersection_finder(l1, l2):
    """Find intersecting node between two linked lists."""
    l1_count, l2_count = 0, 0
    temp_l1, temp_l2 = l1, l2
    while temp_l1:  # get len of l1
        temp_l1 = temp_l1.next
        l1_count += 1
    while temp_l2:  # get len of l2
        temp_l2 = temp_l2.next
        l2_count += 1

    long_ll = l1 if l1_count > l2_count else l2  # determine the longer ll
    short_ll = l2 if l2_count > l1_count else l1  # determine the shorter ll
    short_count = l1_count if l1_count < l2_count else l2_count
    diff = abs(l1_count - l2_count)  # diff between the lens

    for _ in range(diff):  # cut off long ll head to make it as long as short ll
        long_ll = long_ll.next

    for _ in range(short_count):  # loop through both ll together
        if long_ll.next is short_ll.next:  # if they share same node will reflect here
            return long_ll.next.val
        else:  # keep iterating
            long_ll = long_ll.next
            short_ll = short_ll.next
    return -1


if __name__ == '__main__':
    l1 = LinkedList(1)
    l1.next = LinkedList(2)
    l1.next.next = LinkedList(3)
    l2 = LinkedList(5)
    l2.next = LinkedList(4)
    l2.next.next = l1.next.next
    print('the intersecting node between l1 and l2 is ' + str(intersection_finder(l1, l2)))
