
import sys

sys.stdin = open("파리퇴치_input.txt")


T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]




    total = 0 #전체 사격형 중에 가장 큰 값을 구해야 함으로!
    for row in range(N-M+1): #이렇게 해야 내가 원하는 길이만큼 탐색하는 횟수를 맞출 수 있음,,!  이해하고 외워,,!
        for col in range(N-M+1):
            SUM = 0 #여기서 만들어야! 사각형 하나 다 탐색 돌때마다 값을 비교 할 수 있음!!
            for row_sq in range(row, row + M): #이렇게 해야! 그 만큼! 보게 된다! M길이 만큼 보게 된다!
                for col_sq in range(col, col + M):
                    SUM += MAP[row_sq][col_sq]

            if total < SUM :
                total = SUM

    print("#{} {}".format(tc, total))
