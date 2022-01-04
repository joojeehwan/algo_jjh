import os
import time

def printMAP():
    for row_MAP in MAP:
        for now in row_MAP:
            print(f"{now}", end = "")
        print("")
    time.sleep(0.5)
    os.system("cls")

N = 8
MAP = [[0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0]]


def dfs(row, col):

    MAP[row][col] = "!" #초기값 설정!
    printMAP()

    if row == N - 1 and col == N - 1:
        return True # 기저조건 : 끝날 조건

    MAP[row][col] = "#" # 재귀로 다음번 next_col, next_row가 오면 그 값이 들어가서 0번이 있는 자리에 #이 들어간다!

    dr = [0,0,-1,1]
    dc = [1,-1,0,0]
    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
            continue
        if MAP[next_row][next_col] != 0:
            continue
        if (dfs(next_row, next_col)) :
            return True
    return False

dfs(0,0)