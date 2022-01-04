
import sys

sys.stdin = open("delta_seartch_input.txt")

T = 10

for tc in range(1, T+1):


    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]


    sum = 0
    for row in range(N): #고정
        for col in range(N): #탐색
            dr = [-1, 1, 0, 0] #델타 배열 만들기
            dc = [0, 0, -1, 1]
            for k in range(4):

                next_row = row + dr[k]
                next_col = col + dc[k]

                #조건이 실행되면 안되는 경우를 만들어서 continue하는 게 더 좋은 방법!
                #범위를 벚어나는 조건들을 확인
                if next_col < 0 or next_col < 0 or next_row >= N or next_col >= N :
                    continue

                #절대값을 구현하기 위한 절대값 식 구현
                diff = lst[row][col] - lst[next_row][next_col]
                if (diff < 0):  # 절대값
                    diff *= -1
                sum += diff


    print("#{} {}".format(tc, sum))







