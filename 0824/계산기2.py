
import sys
from io import open

sys.stdin = open("계산기2_input.txt")


T = 10

#후위로 바꾸는 작업이 필요함!


for tc in range(1, T+1):

    N = int(input())
    a = input()
    stack = []
    res = ''
    for x in a:
        if x.isdecimal():
            res += x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()

    result = []

    for target in res:

        if target == "+":
            result.append(result.pop(-2) + result.pop())
        elif target == "*":
            result.append(result.pop(-2) * result.pop())
        else:
            result.append(int(target))

    print("#{} {}".format(tc, result[0]))


    #최교수님 풀이

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
            while len(stack) != 0 and stack[-1] == "*": #연산을 먼저 할것을 뺴어주고 그 다음에 넣는,,!!!
                postfix.append(stack.pop(-1))
            stack.append(ch)
        elif ch == "*":
            stack.append(ch)
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






