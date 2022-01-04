


#팁 : 일반적으로 괄호 문제 대부분이 stack으로 문제 해결

#쇠막대기이ㅡ ㅣ개수는 스택안에 있ㄴ는 "("의 갯수만큼! 

T = int(input())
for tc in range(T):
    str1 = input()
    stack = []
    ans = 0
    for i in range(len(str1)):
        now = str1[i]
        if now == "(":
            stack.append(i)
        else :#닫는 괄호
            pop = stack[-1]
            # 마지막으로 넣었던 값 확인
            stack.pop(-1)
            # 마지막으로 넣었던 값 삭제
            if pop == i - 1: # 여는괄호가 바로 앞에 있었다.
                # 레이저를 쏘는 지점
                ans += len(stack)
            else :
                # 레이저가 아니면 쇠막대기가 끝나는 지점
                ans += 1
    print("#{} {}".format(tc + 1, ans))


# 팁 : 일반적으로 괄호 문제 대부분이 stack으로 해결

        # 팁 : 일반적으로 괄호 문제 대부분이 stack으로 해결