'''

DFS 실전 적용

'''

def dfs(row, col, sum):

    global ans

    if row == N-1 and col == N-1:
        ans = min(ans, sum + MAP[row][col])
        return

    dr = [1, 0]
    dc = [0, 1]
    for i in range(2):
        next_row = row + dr[i]
        next_col = col + dc[i]

        if not (0 <= next_row < N and 0 <= next_col < N):
            continue

        dfs(next_row, next_col, sum + MAP[row][col])


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    ans = 24215781878

    MAP = [list(map(int, input().split())) for _ in range(N)]

    dfs(0,0,0)

    print(ans)


