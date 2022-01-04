


import sys


sys.stdin = open("오목판정_input.txt")
'''

이차원 배열을 받을 입력 받은 후에,

델타 배열을 이용해서 값을 확인한다!

델타 배열로 확인할 곳은 가로 세로 우하향 우상향,, 이렇게,,!

저번에 풀다가 막히면 저번에 풀었던 부분 다시 읽어 본다!

'''



T = int(input())

for tc in range(1, T+1):


    N = int(input())

    MAP = [list(input()) for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if MAP[row][col] == ".":
                MAP[row][col] = 0
            elif MAP[row][col] == "o":
                MAP[row][col] = 1

    flag = 0
    for row in range(N):
        for col in range(N):
            dr = [0, 1, -1, 1]
            dc = [1, 0, 1, 1]
            if MAP[row][col] == 0:
                continue
            for dir in range(4):
                cnt = 0
                for i in range(5):
                    next_row = row + dr[dir] * i
                    next_col = col + dc[dir] * i
                    if next_row < 0 or next_col < 0 or next_col >= N or next_row >= N:
                        continue
                    if MAP[next_row][next_col] == MAP[row][col]:
                        cnt += 1




                if cnt == 5:
                    flag = 1

    if flag == 1:
        print("#{} YES".format(tc))
    else:
        print("#{} NO".format(tc))


# dr = [0, 1, 1, -1]
# dc = [1, 0, 1, 1]
# row = 0
# for dir in range(4):
#     next_row = row + dr[dir] * 5
#
# print(next_row)




'''

dr = [0, 1, 1, 1]  # 행
dc = [1, 1, 0, -1] # 열

def check(r, c):
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        cnt = 1
        while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
            cnt += 1
            nr, nc = nr + dr[i], nc + dc[i]
        if cnt > 4:
            return 1
    return 0

string = ['NO', 'YES']
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [input() for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.': continue
            ans = check(r, c)
            if ans: break
        if ans: break

    print(string[ans])



'''
