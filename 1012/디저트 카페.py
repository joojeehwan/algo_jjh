'''

단순한 dfs 문제라고 생각하자!

'''


def dfs(now_x, now_y, direction, path, start_x, start_y):
    global result
    if direction > 3:
        return

    if direction == 3 and (now_x, now_y) == (start_x, start_y):
        result = max(result, len(path))
        return

    if board[now_x][now_y] in path:
        return

    for i in range(direction, 4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if i == direction:
            dfs(nx, ny, direction, path + [board[now_x][now_y]], start_x, start_y)
        else:
            dfs(nx, ny, direction + 1, path + [board[now_x][now_y]], start_x, start_y)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    result = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, [], i, j)

    print(f'#{tc} {result}')






####################


#교수님 풀이 = > 오류가 있음. 수정해야함

'''

디저트 코드의 dfs에 ret초기값을 0으로 하면 안됐네요
0이된다면 '최대한 갈 수 있는 만큼'가는 형태가 되버릴 수도 있어서 
-2134567890으로 완전 큰 음수값을 넣어주어 정답이 될 수 있는 것 아니면
아무리 더해도 의미가 없도록 해야합니다.

'''

# 디저트

def dfs(row, col, dir, sr, sc):
    # dfs의 return값 : '몇 개의 디저트를 택했는가?'
    if dir >= 4:
        return -2134564890 # 방향을 4번 이상 돌렸다.
    if MAP[row][col] == -1:
        return -2134567890 # 맵 바깥으로 나간다.
    if row == sr and col == sc:
        return 1 # 1가지 방법을 찾았다.
    if check[MAP[row][col]]:
        return -2134567890 # 불가능하다.
    dr = [1,1,-1,-1, 1]
    dc = [1,-1,-1,1, 1]
    check[MAP[row][col]] = True
    ret = 0
    ret = max(ret, dfs(row + dr[dir], col + dc[dir], dir, sr, sc) + 1)
    ret = max(ret, dfs(row + dr[dir + 1], col + dc[dir + 1], dir + 1, sr, sc) + 1)
    check[MAP[row][col]] = False
    return ret

t = int(input())
for tc in range(t):
    n = int(input())
    MAP = [[-1]*(n + 2) for _ in range(n + 2)]
    temp_MAP = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            MAP[i + 1][j + 1] = temp_MAP[i][j]
    check = [False] * 101 # DAT[index], index : 디저트 번호, value : 해당 디저트를 택했는가?
    ans = 0
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            check[MAP[row][col]] = True # 시작점 디저트 체크
            ans = max(ans, dfs(row + 1, col + 1, 0, row, col))
            check[MAP[row][col]] = False # 현재 시작점이 끝나면 기록 삭제
    if ans < 4: # 가능한 방법을 못찾았다.
        ans = -1
    print(f"#{tc + 1} {ans}")


"""

def dfs(row, col, dir, sr, sc, path = []):
    # dfs의 return값 : '몇 개의 디저트를 택했는가?'
    if row == sr and col == sc:
        if len(path) == 5:
            de = 1
        return 1 # 1가지 방법을 찾았다.
    if check[MAP[row][col]]:
        return -2134567890 # 불가능하다.
    if dir >= 4:
        return -2134564890 # 방향을 4번 이상 돌렸다.
    dr = [1,1,-1,-1]
    dc = [1,-1,-1,1]
    check[MAP[row][col]] = True
    ret = 0
    if 0 <= row + dr[dir] < n and 0 <= col + dc[dir] < n:
        ret = max(ret, dfs(row + dr[dir], col + dc[dir], dir, sr, sc, path + [(row, col, MAP[row][col])]) + 1)
    if dir + 1 < 4 and 0 <= row + dr[dir + 1] < n and 0 <= col + dc[dir + 1] < n:
        ret = max(ret, dfs(row + dr[dir + 1], col + dc[dir + 1], dir + 1, sr, sc, path + [(row, col, MAP[row][col])]) + 1)
    check[MAP[row][col]] = False
    return ret

t = int(input())
for tc in range(t):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    check = [False] * 101 # DAT[index], index : 디저트 번호, value : 해당 디저트를 택했는가?
    ans = 0
    for row in range(n - 1):
        for col in range(n - 1):
            check[MAP[row][col]] = True # 시작점 디저트 체크
            if row == 0 and col == 2:
                de = 1
            ans = max(ans, dfs(row + 1, col + 1, 0, row, col))
            check[MAP[row][col]] = False # 현재 시작점이 끝나면 기록 삭제
    if ans < 4: # 가능한 방법을 못찾았다.
        ans = -1
    print(f"#{tc + 1} {ans}")
"""







