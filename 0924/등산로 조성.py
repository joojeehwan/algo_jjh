'''

dfs




tip

1) 삽질할때 현재 높이 - 1 만큼만 깍는다..

2) 비짓 배열을 만들어서 사용



#2가지 경우로 푼다?!

1. 현재 높이를 들고 다니지 않을때

2. 현재 높이를 들고 다닐때!
'''

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(now_row, now_col, path, skill):
    global ans
    #최장 등산로 갱신하기 => 여기서 최장 등산로를 갱신하니!
    if ans < path:
        ans = path

    for i in range(4):
        next_row = now_row + dr[i]
        next_col = now_col + dc[i]

        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
            continue

        if visited[next_row][next_col] == 1:
            continue

        if MAP[now_row][now_col] > MAP[next_row][next_col]:
            visited[next_row][next_col] = 1
            dfs(next_row, next_col, path+1, skill)
            visited[next_row][next_col] = 0

        elif MAP[now_row][now_col] <= MAP[next_row][next_col] and not skill :
            for i in range(1, K+1):
                MAP[next_row][next_col] -= i #공사하기
                skill = True
                #경로로 들어가보고!!
                if MAP[now_row][now_col] > MAP[next_row][next_col]:
                    visited[next_row][next_col] = 1
                    dfs(next_row, next_col, path+1, skill)
                    visited[next_row][next_col] = 0
                #공사 취소 하기!
                skill = False
                MAP[next_row][next_col] += i # 공사한거 다시 올리는 거!

T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]

    #가장 높은 봉우리 찾기!
    MAX = 0
    for row in range(N):
        for col in range(N):
            if MAP[row][col] > MAX:
                MAX = MAP[row][col]


    #입력 받으면서 최고 높이 찾기
    # MAP = []
    # max_high = 0
    #
    # for i in range(N):
    #     #한줄 입력을 받고 내부에서 가장 큰 값을 찾자
    #     tmp = list(map(int, input().split()))
    #
    #     for j in tmp:
    #         if max_high < j:
    #             max_high = j
    #
    #     MAP.append(tmp)

    
    ans = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == MAX:
                visited = [[0] * N for _ in range(N)]
                visited[i][j] = 1
                dfs(i, j, 1, False)
    print(f"#{tc} {ans}")



    # for i in range(N):
    #     for j in range(N):
    #         if MAP[i][j] == MAX:




