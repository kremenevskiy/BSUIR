"""
\d - any digit
\D - any not digit
\w - any alphabet
\s - space
"""

import re

REG = r"-?([+-/*]?(\(|\(-)*\d+|\(|\))*"

REG2 = r"(^[-]?)(([-+*/]{,1})([\(|\(-]*)(\d+)([\(\)])*)*"

def test(s):
    print("yes" if re.fullmatch(REG2, s) else "no")


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

test("1-(-1-3)*4")
test("1-(-1-3)4")
test("1-5(-1-3)")

test("-(2+(-9))")
test("1*(-2)")
print()
# no
test("2+*2")
test("6+(*9)")
test("(2/9)//2")
test("6--5")
test("1*-2")
test("-(2+(--9))")