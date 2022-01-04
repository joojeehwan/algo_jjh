#stack 이용






T = int(input())

for tc in range(1, T+1):

    str1 = input()
    stack = []
    for ch in str1:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)

    print(f"{tc} {len(stack)}")
