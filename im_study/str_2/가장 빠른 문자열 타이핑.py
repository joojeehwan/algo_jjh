
import sys
sys.stdin = open("가장 빠른 문자열 타이핑_input.txt")


T = int(input())

for tc in range(1, T + 1):

    text, patt = input().split()

    i = 0
    ans = 0

    while i < len(text) - len(patt) + 1:
        # 비교를 시작할 기준점 i

        cnt = 0

        for j in range(len(patt)):
            if text[i+j] == patt[j]:
                cnt += 1

        if cnt == len(patt):
            i += len(patt)# 패턴의 수만큼 뛰어 넘어야 하닊나!

        else:
            i += 1

        ans += 1
    #전체 문자 길이 - 지금 문자 위치 = 남은 문자 개수

    ans += len(text) -i

    print("#{} {}".format(tc, ans))


T = int(input())

for tc in range(1, T+1):

    text, patt = input().split()
    
    
    flag = 0 # 찾았다 라는 기록(몇 개의 문자를 건너뛸것인가?)
    
    ans = 0 #버튼을 누르는 횟수


    for i in range(len(text) - len(patt) + 1):
        if flag != 0:
            flag -= 1
            continue

        cnt = 0
        for j in range(len(patt)):
            if text[i + j] == patt[j]:
                cnt += 1

        if cnt == len(patt):
            flag = len(patt) -1

        ans += 1

    ans += len(patt) - 1 -flag
    print("#{} {}".format(tc, ans))
