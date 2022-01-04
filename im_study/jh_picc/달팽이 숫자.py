

import sys


sys.stdin = open("달팽이숫자_input.txt")




T = int(input())


for tc in range(1, T+1):

    N = int(input())


    # 처리를 쉽게 할려고! 장외가 되는 부분을 -1로 바꾸었다.
    MAP = [[-1] * (N+2) for _ in range(N+2)]


    #데이터 전처리 부분! 실제로 값이 들어가는 부분 0으로 만들어주어야 한다!

    for row in range(1, N+1):
        for col in range(1, N+1):
            MAP[row][col] = 0

    #시작값
    row = 1
    col = 0

    dir = 0

    #우 하 좌 상

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    cnt = 1

    while cnt <= N * N :

        next_row = row + dr[dir]
        next_col = col + dc[dir]

        if MAP[next_row][next_col] != 0 : #장외면!

            dir = (dir + 1) % 4

        else: #장외가 아니면 움직여야 하니깐!
            row = next_row
            col = next_col
            MAP[row][col] = cnt
            cnt += 1

    print("#{}".format(tc))
    for row in range(1, N+1):
        for col in range(1, N+1):
            print("{}".format(MAP[row][col]), end = " ")
        print()


# T = int(input())
#
#
# for tc in range(1, T + 1):
#
#     ######기본 데이터 전처리
#     N = int(input())
#
#
#     #달팽이 MAP 을 다 -1로 만들고!
#     # 나중에 범위 벗어나느 것을 확인 하기 위해서!
#
#     MAP = [[-1] * (N + 2) for _ in range(N+2)]
#
#
#     # 값이 들어가는 부분만! 0으로 만들어 준다!
#
#     for row in range(1, N+1):
#         for col in range(1, N+1):
#             MAP[row][col] = 0
#
#     ######이동을 위한 준비
#
#     #우 하 좌 상 의 순서로 움직이는 것을 알고! 그렇게 델타 배열 만들기!
#     dr = [0,1,0,-1]
#     dc = [1,0,-1,0]
#
#     #처음 시작 좌표! => -1 이 있는 그곳,,!
#
#     row = 1
#     col = 0
#
#     #현재 진행중인 방향!
#
#     dir = 0
#     #이게 왜,,,? => 하나씩 적어가면서 기록해야 하니깐!  그리고 언제 까지 적는지도 알려줌!
#     cnt = 1
#     while cnt <= N * N :  # N * N까지의 숫자까지 적게 된다!
#         # 다음 좌펴 가보자아!!
#         next_row = row + dr[dir]
#         next_col = col + dc[dir]
#         #예외 생각,,,!
#         if MAP[next_row][next_col] != 0: #  장외를 만나게 되면! (-1이 이야? => 그럼 장외)
#             dir = (dir + 1) % 4
#             #tip,,,!
#         else:
#             row = next_row
#             col = next_col
#
#             MAP[row][col] = cnt
#
#             cnt += 1
#
#
#     print("#{}".format(tc))
#
#     for row in range(1, N + 1):
#         for col in range(1, N+1):
#             print("{}".format(MAP[row][col]), end = " ")
#
#         print()
#

    
    
    
            
    