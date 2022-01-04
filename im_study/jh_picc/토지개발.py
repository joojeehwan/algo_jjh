

import sys

sys.stdin = open("토지개발_input.txt")


T = int(input())


for tc in range(1, T+1):


    #기본 입력 받기
    N = int(input())

    r1, c1, r2, c2 = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]

    # 평균 구하기
    SUM = 0
    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            SUM += MAP[row][col]


    #평탄화 높이 구함
    avg = SUM // ((r2+1-r1) * (c2+1-c1))

    res = 0
    for row in range(r1, r2 + 1):
        for col in range(c1, c2 + 1):
            res += abs(MAP[row][col] - avg)


    print("#{} {} {}".format(tc,avg, res))
  