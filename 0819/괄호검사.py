




'''
( { => 스택에 push

) ] => pop을 한 후 쌍을 비교

쌍이 맞지 않는다면 에러, 스택이 비어있는데 pop을 하려한다면 에러



'''





T = int(input())

for tc in range(1, T+1):

    test1 = input().rstrip()
    stack = []

    for tes in test1:
        ans = 1 #원래 참이라 가정하고
        if tes == "(" or tes =="}" :
            stack.append(tes)

        elif tes == ")" or tes =="}" : #조건이 거짓인 경우를 생각!
            if not stack:
                ans = 0
                break
            p = stack.pop()
            if  p != "{" or p != "(":
                ans = 0

    if stack:
        ans = 0

    print(f"#{tc} {ans}")