


import sys

sys.stdin = open("coloring_input.txt")






T = int(input())




for tc in range(1, T+1):

    N = int(input())

    #색깔 들이 칠해질,,! 장소를 내가 미리 만든다,,!
    MAP = [[0] * 10 for _ in range(10)]

    colors = [list(map(int, input().splt())) for _ in range(N)]



    #3개가 되어도 쓰일 수 있게 이차워 배열로 받아와서 각각으 컬러에 대한 작용을 한것!
    for color in colors: #컬러를 2차원 배열로 받아서, 하나씩 가져와서!

        garo = color[2] - color[0] + 1
        sero = color[3] - color[1] + 1

        #가로 세로 길이를 구한 다음에!

        start_row, start_col = color[0], color[1]
        # 각각의 시작지점에 맞게 .,,! 만들어서,,!

        for i in range(sero):
            for j in range(garo):
                MAP[start_row + j][start_col + i] += color[4]
        #각각의 변화에 맞게 색을 칠해준다! => 마지막 숫자 값을 적는게 색칠이라 생각!


    cnt = 0
    for i in range(10):
        cnt += MAP[i].count(3)

    print(f"#{tc} {cnt}")
