
import sys
sys.stdin = open("[6기 3회차] A반_알고리즘_과목평가 문제2_in.txt")

T = int(input())



for tc in range(1 ,T+1):


    N = int(input())

    r1, c1, r2, c2 = map(int, input().split()) #이게 왜 기억이 안나,,? 주지환? 흐,, 제발좀,,

    MAP = [list(map(int, input().split())) for _ in range(N)]

    SUM = 0

    #좌표가 주어지면,, 그냥 그점 부터 간다,,! range에 넣을 생각 해라,, 이 놈아,,!
    for row in range(r1, r2 + 1):
        for col in range(c1, c2 + 1):
            SUM += MAP[row][col]

    ave = SUM // ((r2 - r1 + 1) * (c2 - c1 + 1))

    ans = 0
    for row in range(r1, r2 + 1):
        for col in range(c1, c2 + 1):
            diff = MAP[row][col] - ave
            if diff < 0:
                diff *= -1
            ans += diff

    print("#{} {} {}".format(tc, ave, ans))
