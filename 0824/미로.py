# 어제 푼 미로랑 같아! 그래서! 3에서 멈추게 할려면! 기저 조건에

#3에서 멈추라고 하면돼!



# import os
# import time
#
# def printMAP():
#     for row_MAP in MAP:
#         for now in row_MAP:
#             print(f"{now}", end = "")
#         print("")
#     time.sleep(0.5)
#     os.system("cls")


'''


dfs : 갈 수 있는데로 가라!

현재점 => 다음점





왔던 길을 다시 가는 것을 조심하라,,!!! => 비지티드 배욜!


기록을 하기도 전에 기록이 있으면, 그러면 갔던 점이니깐 고려하면 안돼!!
    "갈꺼야" 하기 전에 기록!
    그리고 간다! dfs에 넥스트 로우 넣고 넥스트 col ㄴ허고



기저 조건이 없ㅇ도 잘 돌아가네!?

구조 :
현재점에서 다음점으로 갈 수 있는 점을 발견하면 가라!!!
    if 갈 수 있는 점이 없다면? <- 아무것도 안함!  <- 더 이상 진행 x

위와 같은 이유로 기저 조건이 없어도 잘 돌아가는 것임! 다음점이 없으면 아무것도 안하니깐!




답찾는 요령

1. 전역변수로 기록! ex) ans변수 사용,,! 0에서 1로,,! 3에 도착하면 ans를 1로 바꾸어!
(돌아가는 도중에)

함수 안에서!
if 맵의 정보가 3이다?
    ans = 1

2. 비지티드 배열을 확인함!!
(전부 다 돌고!)
for
    for
        if 도착지의 정보가 3이고 ,비지티드로 가본 적이 있던 곳이면!:
            ans = 1

3. 반환 받아서 처리!

함수 안에서

if 맵의 정보가 3이다?
    return 1

flag = 0 내 이후에 도착지를 발견한적 있ㄴ는가?

함수 밖은?
밑에는 사진 확인해!

'''

# 지금 중요한것은 dfs 구조 잡는 것!


# 디버깅 tip,,! de = 1 이라 놓고, 브레이크 포인트 놓고! 돌린다!


import sys



def dfs(row, col):

    MAP[row][col] = "!" #초기값 설정!
    # printMAP()


    if MAP[row][col] == 3:
        return 1

    MAP[row][col] = "#"


    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]

        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N :
            continue

        if MAP[next_row][next_col] != 0:
            continue

        if (dfs(next_row, next_col)):
            return True
    return  0

sys.stdin = open("미로_input.txt")

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    MAP = [list(map(int, input().rstrip())) for _ in range(N)]


    for row in range(len(MAP)):
        for col in range(len(MAP[row])):

            if MAP[row][col] == 2:

                dfs(row, col)




#교수님 풀이

def dfs(row, col):
    # 반환값 <- 도착지를 발견하면 1, 아니면 0
    """
    global ans
    if MAP[row][col] == 3:
        ans = 1
    """
    if MAP[row][col] == 3:
        return 1

    flag = 0 # 내 이후에 도착지를 발견한 적이 있는가?
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if 0 <= next_row < N and 0 <= next_col < N:
            # 맵 안에 있을 때만 진행
            if MAP[next_row][next_col] == 1:
                continue # 가려는 좌표에 벽이 있다면 무시
            if visited[next_row][next_col] == 1:
                continue # 기록을 하기 전에 이미 기록이 있다? : 갔던 점이다. 무시
            visited[next_row][next_col] = 1
            if ( dfs(next_row, next_col) == 1) :
                # <- 얘가 한번이라도 1이 있으면 내 결과도 1
                flag = 1

            #dfs(next_row, next_col)
    return flag

T = int(input())
for tc in range(T):
    ans = 0
    N = int(input())
    MAP = [ list(map(int, input().rstrip())) for _ in range(N) ]
    visited = [[0] * N for _ in range(N)] # 해당 좌표를 들렸는지 기록

    visited[2][0] = 1
    #dfs(4, 1)
    """
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 3 and visited[row][col] == 1:
                ans = 1"""
    print(dfs(2, 0))



