import sys
sys.stdin = open("스도쿠 검증 _ input.txt")

'''

저번 풀이에서 배운 것 써먹기 내 스타일로!

0. 입력받기

0-1. flag를 만들어서 이상한게 있으면 오류라고 한다! 

1. 1 ~ 9까지의 숫자를 기록할 카운트 배열 만들어서

2. 가로

3. 세로

4. 사각형




'''


T = int(input())

for tc in range(1, T+1):


    MAP = [list(map(int, input().split())) for _ in range(9)]

    flag = 1 #초기 시작 값으르 플래그를 사용



    for row in range(9):
        #가로
        counts_row = [0] * 10 #여기에 위치해야해,,! 왜냐면 다음 행 넘어갈때 다시 0으로 초기화 하고 확인해야 하니깐!
        for col in range(9): #여기 안에서 확인할 생각을 했어야지! 왜냐면 그래야 값을 넣고 확인 하니깐!
            counts_row[MAP[row][col]] += 1

            if counts_row[MAP[row][col]] > 1:  #내가 틀렸던건 이 위치,,! 들어오는 값을 하나씩 비교 했어야 했는데! 그러지 않았다!
                flag = 0



        # de = 1

        #세로
        counts_col = [0] * 10
        for col in range(9):
            counts_col[MAP[col][row]] += 1

            if counts_col[MAP[row][col]] > 1:
                flag = 0
    #
    #
        # 3x3 삼각형
        # 얻어 갈 것이 많음!


        for col in range(9):
            if row % 3 == 0 and col % 3 == 0: #이렇게 함으로서 작은 사각형들의 왼쪽 대각선위의 시작점들을 찾는다,,! 프렉탈과 비슷,,! 큰거에 적용한 기술을 다시 작은 사각형! 너 3*3 사각형 탐색할떄 어떻게 하는데! 그 생각!!
                counts_sq = [0] * 10
                for row_sq in range(row, row + 3):
                    for col_sq in range(col, col + 3):
                        counts_sq[MAP[row_sq][col_sq]] += 1


                if counts_sq[MAP[row_sq][col_sq]] > 1: #이거는 여기에 위치해야해! row_sq랑 col_sq를 다 검색한 후 사각형을 검사 해야 하니깐!
                    flag = 0


    print("#{} {}".format(tc, flag))