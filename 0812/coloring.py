
# 박스를 다룰때 좌표만으로 다룰 수 있다!

import sys

sys.stdin = open("coloring_input.txt")


#일단 10x10격자에 0으로 초기화!





T = int(input())


for tc in range(1, T+1):
    N = int(input())

    map_ = [[0] * 10 for _ in range(10)]

    colors = []
    for _ in range(N):
        colors.append(list(map(int, input().split())))

    # print(colors)

    for color in colors:

        garo = color[2] - color[0] + 1
        sero = color[3] - color[1] + 1


        startX, startY = color[0], color[1]

        for i in range(sero):
            for j in range(garo):
                map_[startX + j][startY + i] += color[4]

    cnt = 0
    for i in range(10):
        cnt += map_[i].count(3)

    print(f"#{tc} {cnt}")



#빨강을 1로 칠하고, 파랑을 2로 칠하면, 보라가 되는 부분은 3이 됨

T = int(input())
for tc in range(T):
    N = int(input())
    red = []
    blue = []
    for i in range(N):
        box = list(map(int, input().split()))
        if box[-1] == 1:
            red += [box]
        if box[-1] == 2:
            blue += [box]
    # box
    # r1, c1, r2, c2
    # 왼쪽 위, 오른쪽 아래
    # min_r,min_c,max_r,max_c
#index: 0,  1,     2,   3
    ans = 0
    # 칼라별 box 1개씩 고르기
    for now_red in red:
        for now_blue in blue:
            # 겹치지 않는지 확인, 겹치지 않는다면 무시
            if now_red[2] < now_blue[0] or now_blue[2] < now_red[0] :
                continue
            if now_red[3] < now_blue[1] or now_blue[3] < now_red[1] :
                continue

            pu_min_row = 0
            if now_red[0] < now_blue[0]: # min_row끼리 비교
                pu_min_row = now_blue[0] # 둘 중 큰쪽
            else :
                pu_min_row = now_red[0]

            pu_min_col = 0
            if now_red[1] < now_blue[1]: # min_col끼리 비교
                pu_min_col = now_blue[1] # 둘 중 큰쪽
            else :
                pu_min_col = now_red[1]

            pu_max_row = 0
            if now_red[2] < now_blue[2]: # max_row끼리 비교
                pu_max_row = now_red[2] # 둘 중 작은 쪽
            else :
                pu_max_row = now_blue[2]

            pu_max_col = 0
            if now_red[3] < now_blue[3]: # max_col끼리 비교
                pu_max_col = now_red[3] # 둘 중 작은 쪽
            else :
                pu_max_col = now_blue[3]
            #보라색 넓이 = 가로길이               *      세로 길이
            now_pu = (pu_max_col - pu_min_col + 1) * (pu_max_row - pu_min_row + 1)
            ans += now_pu
    print("#{} {}".format(tc + 1, ans))
