# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


class StackQueue(object):
    """Queue with two stacks."""

    def __init__(self, vals=None):
        """."""
        self._s1 = []
        self._s2 = []
        if vals:
            for val in vals:
                self.push(val)

    def push(self, val):
        """Same as enqueue."""
        if not self._s2:
            self._s2.append(val)
            return
        for _ in self._s2:  # reverse s2 to s1
            self._s1.append(self._s2.pop())
        self._s1.append(val)  # add to end of s1(top of queue)
        for _ in self._s1:  # flip again to s2, end is deQ val
            self._s2.append(self._s1.pop())

    def pop(self):
        """Same as dequeue."""
        result = self._s2.pop()
        return result

    def peek(self):
        """Peek next dequeue val."""
        return self._s2[-1]

    def empty(self):
        """Return whether queue is empty."""
        return len(self._s2)

