import sys
sys.stdin = open("퍼펙트셔플_input.txt")

'''

idea,, 그냥나누는 것 이 아니라! 인덱스를 선택해서 가보자! 

'''


T = int(input())

for tc in range(1, T+1):


    N = int(input())
    lst = input().split() #이렇게만 해도 배열에 들어네,,?


    print("#{}".format(tc), end = " ")
    pos1 = 0
    pos2 = (N+1) // 2
    for _ in range((N+1) // 2):
        print(lst[pos1], end=" ")
        if pos2 < N :  #아닐 수가 있음,,?
            print(lst[pos2], end= " ")

        pos1 += 1
        pos2 += 1
    print()


#경계 테스트,,!! 범위 처음과 끝값을 한번 보아라!


T = int(input())

for tc in range(1, 1 + T):

    # 단어 수
    n = int(input())

    # 단어
    words = list(map(str, input().split()))

    # 나뉘는 값
    median_num = n // 2

    # 저장 공간
    res = []

    # 값을 추가할 위치 값
    idx = 1

    # 나누기
    # n이 짝수인 경우
    if n % 2 == 0:

        for q in range(n):
            if q < median_num:
                res.append(words[q])
            else:
                res.insert(idx, words[q])
                idx += 2

    else:

        for q in range(n):
            if q < median_num + 1:
                res.append(words[q])
            else:
                res.insert(idx, words[q])
                idx += 2

    print('#{}'.format(tc), *res)
