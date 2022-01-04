
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

pipe = [[], [1, 1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 0]]
connect = [1, 0, 3, 2]

T = int(input())

for tc in range(1, T+1):

    N, M, R, C, L = map(int, input().split())

    #지도정보

    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = [(R, C)]

    visited[R][C] = 1

    ans = 0

    while q:

        now = q.pop(0)
        now_row = now[0]
        now_col = now[1]
        ans += 1
        #시간 제한
        if visited[now_row][now_col] >= L:
            continue
        #사방향 탐색
        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]


            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue

            if visited[next_row][next_col] != 0:
                continue

            if MAP[next_row][next_col] == 0:
                continue

            curr_p = pipe[MAP[now_row][now_col]]
            next_p = pipe[MAP[next_row][next_col]]

            next_i = connect[i]
            if curr_p[i] == 1 and next_p[next_i] == 1:
                visited[next_row][next_col] = visited[now_row][now_col] + 1
                q.append((next_row, next_col))

    print("#{} {}".format(tc, ans))