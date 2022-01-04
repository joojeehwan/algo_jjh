

import sys

sys.stdin = open("오목 판정 _ input.txt")




T = int(input())



for tc in range(1, T+1):

    N = int(input())

    MAP = [input().rstrip() for _ in range(N)]

    flag = 0 #처음엔 거짓이라 생각하고 , 오목을 완성하면 flag를 1로 바꾼다!


    for row in range(N):
        for col in range(N):
            dr = [0, 1, 1, -1]
            dc = [1, 0, 1, 1]
            # row,col기준에서 나아갈 방향 4가지 선정(오른쪽, 아래, 우하향, 우상향)

            if MAP[row][col] == ".":
                continue

            for dir in range(4): #4가지 방향 다 체크

                cnt = 0

                for i in range(5): #5개의 오목이니깐!

                    next_row = row + dr[dir] * i
                    next_col = col + dc[dir] * i

                    if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                        continue

                    if MAP[next_row][next_col] == MAP[row][col]: #처음거랑 계속 같아 지겟지! 오목은
                        cnt += 1

                if cnt == 5:
                    flag = 1

    if flag == 1:
        print("#{} YES".format(tc))

    else:
        print("#{} NO".format(tc))


# T = int(input())
#
#
# for tc in range(1,T+1):
#
#     N = int(input())
#
#     MAP = [list(input().rstrip()) for _ in range(N)]
#
#     # 가로, 세로, 우상향, 우하향 만 확인하면 된다!
#
#     flag = 0
#
#     for row in range(N):
#         for col in range(N):
#             dr = [0, 1, -1, 1]
#             dc = [1, 0, 1, 1]
#             if MAP[row][col] == ".": #일단 들어가기전에 이게 들어가도 되는지 예외 거르기!
#                 continue
#
#             for dir in range(4):
#
#                 cnt = 0
#
#                 for i in range(5): #이렇게 해서 가로 세로 우하향 우상향으로 5칸을 확인 할 수 있음! 반복 돌면서!
#
#                     next_row = row + dr[dir] * i #곱하면서 옮기는 값을 바꾼다!
#                     next_col = col + dc[dir] * i
#
#                     if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
#                         continue #next의 범위를 조정!
#
#                     if MAP[next_row][next_col] == MAP[row][col]: #오목의 조건! 처음 돌이랑 같아야 하자나! 연속되게!
#                         cnt += 1
#
#                 if cnt == 5:
#                     flag = 1
#
#     if flag == 1:
#         print("#{} YES".format(tc))
#     else:
#         print("#{} NO".format(tc))


###############


# dr = [0, 1, 1, 1]  # 행
# dc = [1, 1, 0, -1] # 열
#
# def check(r, c):
#     for i in range(4):
#         nr, nc = r + dr[i], c + dc[i]
#         cnt = 1
#         while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
#             cnt += 1
#             nr, nc = nr + dr[i], nc + dc[i]
#         if cnt > 4:
#             return 1
#     return 0
#
# string = ['NO', 'YES']
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     board = [input() for _ in range(N)]
#
#     ans = 0
#     for r in range(N):
#         for c in range(N):
#             if board[r][c] == '.': continue
#             ans = check(r, c)
#             if ans: break
#         if ans: break
#
#     print(string[ans])
#
#


