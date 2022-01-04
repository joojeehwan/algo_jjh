
import sys


sys.stdin = open("sum_input.txt")




T = 10


for _ in range(1, T+1):

    tc = int(input())

    MAP = [list(map(int,input().split())) for _ in range(100)]

    n = 100
    #가로 / 세로

    total = 0

    for row in range(n):
        sum_row = 0
        for col in range(n):
            sum_row += MAP[row][col]

        if total < sum_row:
            total = sum_row

        sum_col = 0
        for col in range(n):
            sum_col += MAP[col][row]

        if total < sum_col:
            total = sum_col

    #우상향 대각선
    sum_dia_up = 0
    for i in range(n):
        sum_dia_up += MAP[i][i]

    if total < sum_dia_up:
        total = sum_dia_up

    #우하향 대각선
    sum_dia_down = 0
    for i in range(n):
        sum_dia_down += MAP[i][n-1-i]

    if total < sum_dia_down:
        total = sum_dia_down


    print("#{} {}".format(tc, total))
    
    
    


    
    
