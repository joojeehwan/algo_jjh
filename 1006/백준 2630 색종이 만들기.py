# 2630 색종이 만들기
import sys

ans_white = 0
ans_blue = 0

def check(row, col, size):
    for r in range(row, row + size):
        for c in range(col, col + size):
            if MAP[row][col] != MAP[r][c]:
                return False
    return True

def func(row, col, size, div = 2):
    global ans_blue
    global ans_white
    c = check(row, col, size) # <- row,col을 시작으로 size*size에 하나의 색종이로 표현이 가능한가?

    if c :
        if MAP[row][col] == 1:
            ans_blue += 1
        elif MAP[row][col] == 0:
            ans_white += 1
    else:
        for nr in range(row, row + size, size//div):
            for nc in range(col, col + size, size//div):
                func(nr, nc, size//div)
        """
        func(row, col, size // 2)
        func(row, col + size//2, size//2)
        func(row + size//2, col, size//2)
        func(row + size//2, col + size//2, size//2)
        """


n = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

func(0, 0, n)
print(ans_white)
print(ans_blue)






# [1,2,3,4,5,6,7,8,9,10]
# def func(left, right):
#     mid = (left + right) // 2
#     func(left, mid)
#     func(mid, right)
#
#
#
# def func(lu_row, lu_col, rd_row, rd_col):
#     mid_row, mid_col = (lu_row + rd_row) // 2, (lu_col, rd_col) // 2
#     func(lu_row, lu_col, mid_row, mid_col)
#     func(mid_row + 1, lu_col, rd_row, mid_col)
#     ...
#     ...
#     size_row = rd_row - lu_row
#     size_col = rd_col - lu_col
#     for nr in range(lu_row, rd_row):
#         for nc in range(lu_col, rd_col):
#             func(nr, nc, nr + size_row, nc + size_col)