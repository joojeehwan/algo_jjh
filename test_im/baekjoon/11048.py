

'''


다이나믹이라고 하지만 dfs로 풀 수 있을거 같다!

다이나믹으로 풀어볼까?!

점화식을 만들어서! 시간 초가 뜨면 dp반환으로 해보자,,!


최소 최단이면 bfs로 하면 될거 같은데! dfs로 해서 max값을 구하면 될 것 같ㄷ.


'''


import sys

sys.setrecursionlimit(int(1e7))

def dfs(now_row, now_col):

    if now_row == N-1 and now_col == M-1:
       return MAP[now_row][now_col]


    if dp[now_row][now_col] != -1:
        return dp[now_row][now_col]

    # 하 우하 우
    dr = [1, 1, 0]
    dc = [0, 1, 1]

    ret = 0

    for i in range(3):

        next_row = now_row + dr[i]
        next_col = now_col + dc[i]


        #이 부분이 중요!!
        if not (0 <= next_row < N and 0 <= next_col < M ):
            continue

        ret = max(ret, dfs(next_row, next_col) + MAP[now_row][now_col])

    dp[now_row][now_col] = ret
    return ret


N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]

ans = dfs(0,0)

print(ans)



