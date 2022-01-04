#담당 교수님 풀이가 더 통일 성 있음,,,! 델타 배열,,!


'''


사다리 타기 생각!

아래에서 위로 올라가는게 낫지 않아?
왜냐면 실제로도 값 알면 확인 할려고 밑에서 위로 올라가니깐,,!


'''


import sys
sys.stdin = open("ladder1_input.txt")


T = 10

for _ in range(1, T+1):


    #기본 입력
    tc = int(input())

    size = 100

    MAP = [list(map(int, input().split())) for _ in range(size)]

    visited = [[0] * size for _ in range(size)]


    #시작점 찾기

    row = size - 1
    col = 0

    for i in range(size):
       if MAP[row][i] == 2 :
           col = i


    #한번 움직거려 보자아,,! 좌 , 우 , 상 (위로 올라가는 것이니깐!)

    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    #정확한 목표, 확실하지 않은 반복 횟수,, -> while
    while row > 0 :

        for i in range(3):

            next_row = row + dr[i]
            next_col = col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size :
                continue

            if visited[next_row][next_col] == 1:
                continue

            if MAP[next_row][next_col] == 1:
                row = next_row
                col = next_col
                visited[row][col] == 1
                break

    print("#{} {}".format(tc, col))


# T = 10
#
# for tc in range(T):
#
#     #기본입력
#     N = int(input())
#     size = 100
#     MAP = [list(map(int, input().split())) for _ in range(size)]
#
#     # 한번 간곳은 저장하기 위한 "기억 배열 만들기"
#     visited = [[0] * size for _ in range(size)]
#
#
#     #끝에서 부터 시작점 찾기!
#     row = size - 1 #인덱스니깐,,! 0 ~ 99
#     col = 0
#     for i in range(size):
#         if MAP[row][i] == 2: #대각선 왼쪽 아래서부터 값을 찾아나간다,,!
#             col = i
#
#     #사다리 타고 올라가기!
#     # 우선순위 : 기본은 위로 올라가기이지만, 왼쪽이나 오른쪽이 있으면
#     # 왼쪽 오른쪽이 먼저이다!
#
#     #좌, 우 , 상
#     dr = [0, 0, -1]
#     dc = [-1, 1, 0]
#
#     #while문은 자주 쓰인다,,! 어느 목표에 대해서 갈때! 값을 하니씩 증가 시키면서 볼때
#     #목표는 정확히 있는데, 거기까지의 전체 반복수를 모를때,,?! 하나씨 증가혹은 감소 시키면서 접근!
#     while row > 0 : # 밑에서 부터 올라가니깐! row가 0보다 끌떄까지 간다! 도착지 까지 간다!
#
#         for i in range(3) : # 방향 정해서 한칸!
#             next_row = row + dr[i]
#             next_col = col + dc[i]
#             if next_row <0 or next_col < 0 or \
#                 next_row >= size or next_col >= size:
#                 continue #맵을 벗어나는 좌표면 무시
#             if visited[next_row][next_col] == 1:
#                 continue
#             if MAP[next_row][next_col] == 1:
#                 row = next_row # 아 여기서 row를 건드리니깐! 굳이 row에 대한 조건을 걸지 않는다!
#                 col = next_col
#                 visited[row][col] = 1 #방문 했기 때문에 표시한다
#                 break #굳이 다른 방향을 볼 필요가 없으니! break로 나간다!
#
#         # 2차원 맵, 델타 배열로 다음 좌표를 계산해서 움직이는 경우
#         # 좌표 계산시 맵을 벗어나는 좌표가 찾아지는 경우
#
#         # 갔던 곳을 다시 가는 경우
#     print("#{} {}".format(tc, col))




