# Given a list, rotate the list to the right by k places, where k is non-negative.


# Example:

# Given 1->2->3->4->5->NULL and k = 2,

# return 4->5->1->2->3->NULL.


class LinkedList(object):
    """Simple linked list class."""

    def __init__(self, val):
        """."""
        self.next = None
        self.val = val


def rotated_list(ll, k):
    """Pivot linked list with index k."""
    prev = LinkedList(None)  # init null node before head
    prev.next = ll  # link null node to head
    p1, p2 = prev, prev  # two pointers both at null node

    for _ in range(k):  # move p1 so p1 and p2 are n node apart
        p1 = p1.next

    while p1.next:  # move both p1,p2 together to end
        p1 = p1.next
        p2 = p2.next
    p1.next = ll  # p1 is now tail, link to org head
    new_head = p2.next  # new head is p2 (pivot) next node
    p2.next = None  # pivot node next should be null (pivot not tail)
    return new_head


if __name__ == '__main__':
    ll = LinkedList(1)
    ll.next = LinkedList(2)
    ll.next.next = LinkedList(3)
    ll.next.next.next = LinkedList(4)
    ll.next.next.next.next = LinkedList(5)
    ll.next.next.next.next.next = None
    print('after rotation at k=2 1->2->3->4->5 becomes 4->5->1->2->3')
