

import sys

sys.stdin = open("forth_input.txt")


# lst = [1,2]
#
# result = lst.pop(-2)
#
# print(result)



T = int(input())

for tc in range(1, T + 1):

    lst = input().split()

    stack = []

    try:
        for i in lst:
            if i ==".":
                res = stack.pop()
                if len(stack) != 0 :
                    res = "error"
                break

            elif i == "+":
                stack.append(stack.pop(-2) + stack.pop())

            elif i == "-":
                stack.append(stack.pop(-2) - stack.pop())

            elif i == "*":
                stack.append(stack.pop(-2) * stack.pop())

            elif i == "/":
                stack.append(stack.pop(-2) // stack.pop())

            else:
                stack.append(int(i))

    except:
        res = "error"

    print('#{} {}'.format(tc, res))
    
    
    
    ######################################
    
    
    #최교수님 풀이

    T = int(input())
    for tc in range(T):
        li = input().split()
        stack = []
        ans = ""
        for ch in li:
            # 연산자
            # 남는 얘들 : 숫자
            if ch == "+":
                if len(stack) < 2:
                    ans = "error"
                    break
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(a + b)
            elif ch == "*":
                if len(stack) < 2:
                    ans = "error"
                    break
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(a * b)
            elif ch == "-":
                if len(stack) < 2:
                    ans = "error"
                    break
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(b - a)
            elif ch == "/":
                if len(stack) < 2:
                    ans = "error"
                    break
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(b // a)
            elif ch == ".":
                ans = stack.pop(-1)
                break
            else:
                stack.append(int(ch))

        if len(stack) != 0:
            ans = "error"
        print("#{} {}".format(tc + 1, ans))
    

