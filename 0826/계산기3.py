T = 10
for tc in range(T):
    N = int(input())
    infix = input()
    stack = [] # 연산자를 잠시 저장해두는 위치
    postfix = [] # 후위표기법
    for ch in infix:
        if "0" <= ch <= "9":
            postfix.append(ch)
        elif ch == "+":
            while len(stack) != 0 and stack[-1] == "*":
                postfix.append(stack.pop(-1))
            stack.append(ch)
        elif ch == "*":
            stack.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while len(stack) != 0 and stack[-1] != "(":
                postfix.append(stack.pop(-1))
            stack.pop(-1)
    while stack: # 남은 연산을 모두 넣어준다.
        postfix.append(stack.pop(-1))

    for now in postfix:
        if "0" <= now <= "9":
            stack.append(int(now))
        elif now == "+":
            a = stack.pop(-1)
            b = stack.pop(-1)
            stack.append(a + b)
        elif now == "*":
            a = stack.pop(-1)
            b = stack.pop(-1)
            stack.append(a * b)
    print("#{} {}".format(tc + 1, stack[-1]))