


#이동하는 dfs라고 생각하자!


#path를 만들어서! 내가 지금까지 온 거리를 기억하게 함!  = > 그래서 중복을 피하는?!
#시작점은 인자로 기록
def dfs(now_row, now_col, dir, path, start_row, start_col):

    global max_res

    #기조 조건
    if dir == 3 and now_row == start_row and now_col == start_col:
        max_res = max(max_res, len(path))
        return

    #한번 간곳은 가지 않는다
    if MAP[now_row][now_col] in path:
        return

    #우하, 좌하, 좌상, 우상
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    #4방향 다 갈 필요가 없으니! next를 가면서
    for i in range(dir, 4):

        next_row = now_row + dr[i]
        next_col = now_col + dc[i]

        if next_row < 0 or next_col < 0 or next_row >=  N or next_col >= N:
            continue

        #현재 방향과 같은 방향으로 이동
        if dir == i:
            dfs(next_row, next_col, dir, path +[MAP[now_row][now_col]], start_row, start_col)

        #현재 방향과 다른 방향으로 이동
        else:
            dfs(next_row, next_col, dir + 1, path +[MAP[now_row][now_col]], start_row, start_col)




T = int(input())


for tc in range(1, T+1):

    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)]

    max_res = -1
    #하나의 점에서만 검사를 해보는게 아니라 모든점에서 검사를 해봐야 함! MAP에 있는 모든 점에서 구현을 해봐야 ㅎ마
    for row in range(N - 1):
        for col in range(1, N - 1):
            dfs(row, col, 0, [], row, col)

    print(f'#{tc} {max_res}')

