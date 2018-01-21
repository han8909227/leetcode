
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


def valid_parentheses(s_parens):
    """."""
    if not s_parens:
        return False
    stack = []
    left = '({['
    right = ')}]'
    for c in s_parens:
        if c in left:
            stack.append(c)  # push left in
        elif c in right:
            try:
                temp = stack.pop()  # try to pop out the left
            except IndexError:
                return False
            if temp != left[right.index(c)]:  # if not what is suppose to closed(last left inserted)
                return False
    return True if not stack else False  # if any left still in stack(unclosed)
