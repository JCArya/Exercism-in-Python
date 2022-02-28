
import inspect
from itertools import chain
import string
OPS = {
    '+':    lambda x, y: [y + x],
    '-':    lambda x, y: [y - x],
    '*':    lambda x, y: [y * x],
    '/':    lambda x, y: [y // x],
    'dup':  lambda x:    [x, x],
    'drop': lambda _:    [],
    'swap': lambda x, y: [x, y],
    'over': lambda x, y: [y, x, y],
}
class StackUnderflowError(Exception):
    def __init__(self):
        super().__init__('Insufficient number of items in stack')
class ZeroDivisonError(Exception):
    def __init__(self):
        super().__init__('divide by zero')
def is_number(elem):
    return elem and (set(elem) < set(string.digits)
                     or (elem[0] == '-' and is_number(elem[1:])))
def apply(stack, elem):
    if is_number(elem):
        stack.append(int(elem))
    elif elem in OPS:
        op = OPS[elem]
        count = len(inspect.signature(op).parameters)
        print(elem, count)
        if len(stack) < count:
            raise StackUnderflowError
        stack.extend(op(*(stack.pop() for x in range(count))))
    else:
        raise ValueError('undefined operation')
def substitute(custom, elems):
    return list(chain(*(custom[x] if x in custom else [x] for x in elems)))
def evaluate(input_data):
    stack = []
    custom = {}
    try:
        for line in input_data:
            elems = line.lower().split()
            if elems[0] == ':':
                assert elems[-1] == ';'
                op = elems[1]
                if is_number(op):
                    raise ValueError('illegal operation')
                custom[op] = substitute(custom, elems[2:-1])
            else:
                elems = substitute(custom, elems)
                for elem in elems:
                    apply(stack, elem)
        return stack
    except ZeroDivisionError:
        raise ZeroDivisionError('divide by zero') # come on now exercism
