'''

① 최초 각 미생물 군집의 위치와 군집 내 미생물의 수, 이동 방향이 주어진다.
  약품이 칠해진 부분에는 미생물이 배치되어 있지 않다. 이동방향은 상, 하, 좌, 우 네 방향 중 하나이다.

② 각 군집들은 1시간마다 이동방향에 있는 다음 셀로 이동한다.

③ 미생물 군집이 이동 후 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고, 이동방향이 반대로 바뀐다.
   미생물 수가 홀수인 경우 반으로 나누어 떨어지지 않으므로, 다음과 같이 정의한다.
   살아남은 미생물 수 = 원래 미생물 수를 2로 나눈 후 소수점 이하를 버림 한 값
   따라서 군집에 미생물이 한 마리 있는 경우 살아남은 미생물 수가 0이 되기 때문에, 군집이 사라지게 된다,

④ 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐지게 된다.
   합쳐 진 군집의 미생물 수는 군집들의 미생물 수의 합이며, 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 된다.
   합쳐지는 군집의 미생물 수가 같은 경우는 주어지지 않으므로 고려하지 않아도 된다.

M 시간 동안 이 미생물 군집들을 격리하였다. M시간 후 남아 있는 미생물 수의 총합을 구하여라.

'''


# # T = int(input())
# #
# # for tc in range(1, T + 1):
#
# #K개의 군집, M시간 후의 미생물의 수, N*N의 정사각형 셀
# N, M, K = map(int, input().split())
#
# MAP = [[-1] * N for _ in range(N)]
#
# #빨간색 부분을 -1로 만들기!
# for i in range(1, N-1):
#     for j in range(1, N-1):
#         MAP[i][j] = 0
#
# for _ in range(K):
#     row, col, number, dir = map(int, input().split())
#
#     MAP[row][col] = (number, dir)
#
# print(MAP)





# n, m, k = map(int, input().split())
#
# MAP = [list(map(int, input().split())) for _ in range(k)]
#
# print(MAP)

N = 7

#return에 or / and 연산이 가능함

'''

1) A and B

- A,B 둘 다 참이면 B 를 출력

- A,B 둘 다 거짓이면 A 를 출력

- A, B 둘 중에 하나만 참이면 거짓인 값을 출력

 

2) A or B

- A,B 둘 다 참이면 A 를 출력

- A,B 둘 다 거짓이면 B 를 출력

- A, B 둘 중에 하나만 참이면 참인 값을 출력

'''

def check_range(row, col):
    #하나라도 바깥 경계에 있으면 True를 반환
    return row == 0 or row == N-1 or col == 0 or col == N-1

def change_dir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    elif dir == 4:
        return 3


def move(MAP):
    new_MAP = [[[] for _ in range(N)] for _ in range(N)]

    #평범한 이동
    for row in range(N):
        for col in range(N):
            if MAP[row][col]:
                #리스트안의 튜플이라! 그래서 [0]까지 필요한것! 데이터 구조 그려보면 쉽게 알 수 있음
                number, dir = MAP[row][col][0]
                next_row = row + dr[dir]
                next_col = col + dc[dir]
                if check_range(next_row, next_col):
                    number //= 2
                    dir = change_dir(dir)

                if number > 0:
                    new_MAP[next_row][next_col].append((number, dir))

    #하나의 셀로 여러개의 미생물이 왔을 떄
    for row in range(N):
        for col in range(N):
            #하나의 셀로 여러개가 온 경우
            if len(new_MAP[row][col]) >= 2:
                total = 0
                max_number, direction = 0, 0
                while new_MAP[row][col]:
                    number, dir = new_MAP[row][col].pop()
                    total += number

                    #while문으로 안에 있는 값들을 한번씩 돌면서
                    #위에서 일단 더하고 아래에선 방향을 정하기 위해서 가장 큰 값을 찾기!

                    if number > max_number:
                        max_number = number
                        direction = dir

                #반복이 끝나고 나면
                new_MAP[row][col].append((total, direction))

    return new_MAP


T = int(input())

for tc in range(1, T + 1):

    N, M, K = map(int, input().split())
    MAP = [[[] for _ in range(N)] for _ in range(N)]

    #문제에서 상하 좌우의 값이 1, 2, 3, 4 이므로 앞에 0을 넣어서 맞춤
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    for _ in range(K):
        row, col, number, dir = map(int, input().split())
        MAP[row][col].append((number, dir))

    for _ in range(M):
        MAP = move(MAP)


    ans = 0
    for row in range(N):
        for col in range(N):
            #무의미한 반복을 없애기 위해서 while문에 조건을 준다.
            while MAP[row][col]:
                number, dir = MAP[row][col].pop()
                ans += number

    print(f"#{tc} {ans}")

