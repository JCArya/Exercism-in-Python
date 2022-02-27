from operator import add, sub, mul, floordiv
def answer(question):
    for s in ["What is", "by", "?"]:
        question = question.replace(s, "")
    operators = {"plus": add, "minus": sub, "multiplied": mul, "divided": floordiv}
    nums, ops = [], []
    for token in question.split():
        if token.isnumeric() or (token.startswith("-") and token[1:].isnumeric()):
            nums.append(int(token))
        else:
            try:
                ops.append(operators[token])
            except KeyError:
                raise ValueError("unknown operation")
        
        if len(nums) == 2 and len(ops) == 1:
            op, b, a = ops.pop(), nums.pop(), nums.pop()
            nums.append(op(a, b))
        if (len(ops) == 1 and len(nums) == 0) or (len(nums) == 2 and len(ops) != 1):
            raise ValueError("syntax error")
    if len(nums) != 1 or len(ops) != 0:
        raise ValueError("syntax error")
    return nums[0]
