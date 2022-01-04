

import sys
sys.stdin = open("퍼펙트셔플_input.txt")



T = int(input())



for tc in range(1, T+1):

    N = int(input())

    str_input = input().split() #이렇게만 해도 리스트에 들어간다구!

    half = N // 2

    res = []

    idx = 1

    #나누기
    #n이 짝수인 경우
    if N % 2 == 0:

        for i in range(N): #입력 문자를 반반 나누어서, 일단 그거전에는 다 넣고, 그 다음엔
                            #인서트 써서 쉽게,,!
            if i < half:
                res.append(str_input[i])
            else:
                res.insert(idx, str_input[i])
                idx += 2

    else:
        for i in range(N):
            if i < half + 1:
                res.append(str_input[i])

            else:
                res.insert(idx, str_input[i])
                idx += 2



    print("#{}".format(tc), *res)  #오,, 리스트 자체를 출력하는 새로운 방법! 조인과 다른!




    ##################################

    T = int(input())

    for tc in range(1, T + 1):

        N = int(input())
        lst = input().split()  # 이렇게만 해도 배열에 들어네,,?

        print("#{}".format(tc), end=" ")
        pos1 = 0
        pos2 = (N + 1) // 2
        for _ in range((N + 1) // 2):
            print(lst[pos1], end=" ")
            if pos2 < N:  # 아닐 수가 있음,,?
                print(lst[pos2], end=" ")

            pos1 += 1
            pos2 += 1
        print()