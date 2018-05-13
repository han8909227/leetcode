# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


class LinkedList(object):
    """Simple linked list class."""

    def __init__(self, val):
        """."""
        self.next = None
        self.val = val


def reorder_ll(head):
    """LC143."""
    if not head:
    	return None

	fast = slow = head

	# determine the mid point, since fast is twice as fast as slow
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next

		# break up the ll into two ll from mid point
		head_1, head_2 = head, slow.next
		slow.next = None

		# reverse the second ll
		cur, pre = head_2, None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        # merge them with the reorder sequence
        cur1, cur2 = head_1, pre
        while cur2:
            nex1, nex2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = nex1
            cur1, cur2 = nex1, nex2



