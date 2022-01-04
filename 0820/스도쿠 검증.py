'''



함수는 retrun 만나면 바로 종료,,! 그냥 포문이 몇개가 되든,,!


이건 풀어볼만하다!


합이 45로 하는건 틀린 것!
반례가 존재!!

인덱스로 하나씩 체크! 체크 배열을 만들어서!

가로 세로 삼삼 검사!


삼삼검사는 어케함?  => 삼으로 나누었을때
=? 4중 포문!! 큰 걸 축소해서 한다고 생각!
반복계수 안 겹치게!
'''
from builtins import str


def check():

    for i in range(9):
        # 체크를 위한 체크 배열 만들기
        row = [0] * 10 #인덱스가 들어오는 숫자의 값이 되고, 값이 그 숫자가 몇개나 들어오나,,! 이번의 경우에는
        # 무조건 하나씩 만 있어야 겠지!
        col = [0] * 10

        for j in range(9):
            #행 검사
            num_row = sudoku[i][j]
            #열 검사
            num_col = sudoku[j][i]

            #이미 사용한 숫자라면 너 멈춰!
            if row[num_row]: return 0
            if col[num_col]: return 0

            row[num_row] = 1
            col[num_col] = 1


            #이거는 내가 몰랐던,,! 새로운 방법! 필기하자!
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10 #체크를 위한 배열!

                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = sudoku[r][c]
                        if square[num]: return 0
                        square[num] = 1

    return 1


T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split()))for _ in range(9)]

    print("#{} {}".format(tc, check()))

            
            


















