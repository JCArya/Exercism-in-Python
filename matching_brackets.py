def is_paired(input_string):
    stack = []
    top_ch = ''
    for ch in input_string:
        if ch == '{' or ch == '[' or ch == '(':
            stack.append(ch)
            top_ch = stack[-1]
        elif (ch == '}' and top_ch == '{') or \
                (ch == ']' and top_ch == '[') or \
                (ch == ')' and top_ch == '('):
            if len(stack) > 0:
                stack.pop()
                top_ch = ''
            if len(stack) > 0:
                top_ch = stack[-1]
        elif (top_ch == '' or top_ch == '{' or top_ch == '[' or top_ch == '(') and \
                (ch == '}' or ch == ']' or ch == ')'):
            return False
    return len(stack) == 0       