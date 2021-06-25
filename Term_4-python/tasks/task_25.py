import  re
def check_balance(str):
    stack = []
    for i in str:
        if re.fullmatch(r"[\(|\[\{]", i):
            stack.append(i)
        if re.fullmatch(r"[\)|\]\}]", i):
            if len(stack) < 1:
                return False
            check_with = stack.pop()
            if check_with == '(':
                if i == ')':
                    continue
                else:
                    return False
            elif check_with == '[':
                if i == ']':
                    continue
                else:
                    return False
            elif check_with == '{':
                if i == '}':
                    continue
                else:
                    return False
    return len(stack) == 0


print(check_balance("[[([()])]]"))