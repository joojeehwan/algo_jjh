


def dfs (row, col): # now : row,col의 위치
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        # now -> next로 갈 수 있으면 가라!
        if next_row < 0 or next_col < 0 or next_row >= h or next_col >= w:
            continue
        if MAP[next_row][next_col] == 1 and visited[next_row][next_col] == 0:
            # 나랑 인접한 곳이 땅이다!
            visited[next_row][next_col] = 1
            dfs(next_row, next_col)

# 맵을 벗어나는 좌표가 계산

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    MAP = [ list(map(int, input().split())) for _ in range(h) ]
    visited = [[0] * w for _ in range(h)]
    # visited[row][col] <- 1 : row,col을 들린적있다. 0 : row, col를 들린적 없다.
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(i, j)
                de = 1
    # 가로크기 w, 세로크기 h