'''

함수로 뺴는 연습 하기 좋네!

봄버맨

구현 / 시물레이션 문제,, 해보자! 쫄지 말자!

해보자!



시간에 따라 변하는구나,, 초기 입력값 주어지고 처음 1초는 아무것도 안하네!

함수를 4개 정도 만들까?!

1) 폭탄의 위치를 찾는 함수

2) 폭탄이 없는 곳에 폭탄을 설치하는 함수

3) 폭탄을 터트리는 함수

4) 격자판 출력하는 함수

시간이 지남에 따라 변하니깐,, while문 써서 시간이 지남을 조건으로 써볼까..!

폭탄이 있는 곳을 저장해야겠네,,! 왜냐면 폭탄위치 기준으로 폭탄이 터지니깐!

일단 초기 세팅은 초기 입력으로 주어지니깐!



1. 초기 입력받기

2. 아무것도 안하기

3. 폭탄이 없는 곳에 폭탄 설치

4. 폭탄 터드리기! 

5. 3) 4) 반복


뭐가 틀린거징?! 인덱스에러?!


'''

import sys

#벡터 배열 그냥 전역변수로 쓰자 또 언제 쓸지 모르자나! 

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


#폭탄의 위치를 찾는 함수! 터지기전에 폭탄이 어디있는지 알아야 하자나!
def search_bomb():
    for row in range(R):
        for col in range(C):
            if MAP[row][col] == "O":
                bomb_locations.append((row, col))

def install_bomb():
    
    #폭탄이 없는 곳 찾아서 폭탄 설치
    for row in range(R):
        for col in range(C):
            if MAP[row][col] == ".":
                MAP[row][col] = "O"


def bomb_expldes():
    #폭탄이 설치 된 곳 상하 좌우에 폭탄이 터진다! 연쇄반응 x
    while bomb_locations:
        now = bomb_locations.pop(0)
        bomb_row = now[0]
        bomb_col = now[1]
        #폭탄이 있는곳도 변해야 하니깐 초기값 넣자마자 바꾸자
        MAP[bomb_row][bomb_col] = "."

        for i in range(4):

            next_bom_row = bomb_row + dr[i]
            next_bom_col = bomb_col + dc[i]

            #경계 벗어나는 곳 제외
            if next_bom_row < 0 or next_bom_col < 0 or next_bom_row >= R or next_bom_col > C :
                continue

            #폭탄이 터짐
            MAP[next_bom_row][next_bom_col] = "."


def print_MAP():

    for row in range(R):
        for col in range(C):
            print(MAP[row][col], end=" ")
        print() #줄 마다 변경 해야 하니깐!


#R, C, N 입력받기
R, C, N = map(int, sys.stdin.readline().split())

#초기 격자판 입력받기

#1 단계 폭탄 설치 함
MAP = [list(sys.stdin.readline()) for _ in range(R)]

bomb_locations = []

# 아 1초동안 아무것도 안하지..!
N -= 1

if N == 0:
    print_MAP()

#3 - 4 단계 반복
else:
    while N:
        #3 단계

        search_bomb()
        install_bomb()
        #시간 줄이기
        N -= 1

        if N == 0:
            break
        #4단계
        #폭탄 터르리기
        bomb_expldes()
        N -= 1

    print_MAP()





