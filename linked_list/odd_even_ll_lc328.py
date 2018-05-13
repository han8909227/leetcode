
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.

# Note:
# The relative order inside both the even and odd groups should remain as it was in the input. 
# The first node is considered odd, the second node even and so on ...


class LinkedList(object):
    """Simple linked list class."""

    def __init__(self, val):
        """."""
        self.next = None
        self.val = val


def odd_even_ll(head):
    """LC 328."""
    odd = LinkedList(None)
    even = LinkedList(None)
    odd_head = odd
    even_head = even

    count = 1

    while head:
    	if count % 2 == 0:
    		even.next = head
    		even = even.next
    	else:
    		odd.next = head
    		odd = odd.next
		temp = head.next
		head.next = None
		head = temp
    	count += 1
    odd.next = even_head.next
    return odd_head.next





if __name__ == '__main__':
    ll = LinkedList(1)
    ll.next = LinkedList(2)
    ll.next.next = LinkedList(3)
    ll.next.next.next = LinkedList(4)
    ll.next.next.next.next = LinkedList(5)
    ll.next.next.next.next.next = None

    





