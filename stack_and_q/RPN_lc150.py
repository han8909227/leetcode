# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# Seen this question in a real interview before?  YesNo
import operator


def rpn(tokens):
    """."""
    stack = []
    op = '+-*/'
    operation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv  # same as // in python
    }

    for num in tokens:
        if num not in op:
            stack.append(int(num))
        else:
            val_1 = stack.pop()
            val_2 = stack.pop()
            re = operation[num](val_2, val_1)
            stack.append(re)
    return stack.pop()


if __name__ == '__main__':
    a = ["2", "1", "+", "3", "*"]
    b = ["4", "13", "5", "/", "+"]
    print('RPN for ' + str(a) + ' is ' + str(rpn(a)))
    print('RPN for ' + str(b) + ' is ' + str(rpn(b)))
