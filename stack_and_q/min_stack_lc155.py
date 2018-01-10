# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack(object):
    """Min Stack class."""

    def __init__(self, iterable=None):
        """Init."""
        if iterable:
            for val in iterable:
                self.push(val)
        self._super = []
        self._min = []

    def push(self, val):
        """Push into stack."""
        self._push.append(val)
        curr_min = self.get_min()
        if val <= curr_min:  # if new min val found
            self._min.append(val)

    def pop(self):
        """Pop from the stack."""
        if not self._super:
            raise ValueError('empty stack cannot pop')
        if self._super[-1] == self._min[-1]:  # if popping the min val
            self._min.pop()
        self._super.pop()

    def get_min(self):
        """Get the current min val in stack."""
        if not self._super():  # on init empty stack
            return float('inf')  # to allow val in append in min stack
        else:
            return self._min[-1]  # curr min val
