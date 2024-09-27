def eval_postfix(expr):
    stk = []
    tokens = expr.split()
    
    for t in tokens:
        if t.lstrip('-').isdigit():
            stk.append(int(t))
        else:
            b = stk.pop()
            a = stk.pop()
            if t == '+':
                stk.append(a + b)
            elif t == '-':
                stk.append(a - b)
            elif t == '*':
                stk.append(a * b)
            elif t == '/':
                stk.append(int(a / b))
            elif t == '^':
                stk.append(a ** b)
    
    return stk[0]

test_cases = [
    ("5 6 +", 11),
    ("3 4 2 * 1 5 - 2 3 ^ ^ / +", -1),
    ("-5 6 -", -11),
    ("15 7 1 1 + - / 3 * 2 1 1 + + -", 5),
    ("5", 5)
]

for expr, expected in test_cases:
    result = eval_postfix(expr)
    print(f"Input: {expr}, Output: {result}")

user_expr = input("Enter a postfix expression: ")
user_result = eval_postfix(user_expr)
print(f"Result of '{user_expr}': {user_result}")
