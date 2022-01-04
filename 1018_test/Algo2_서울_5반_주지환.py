
#경로의 갯수 까지 구해보자!

#벡터 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#dfs 사용
def dfs(row, col, path=[]):

    #정답을 찾으면 기록
    global ans
    global cnt
    if MAP[row][col] == 3:
        ans = 1
        return len(path)

    else:
        #델타 배열로 사방 탐색
        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            #범위 벚어나면 탐색x
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            #함정이면 탐색x
            if MAP[next_row][next_col] == 4:
                continue
            #벽이여도 탐색x
            if MAP[next_row][next_col] == 1:
                continue

            # 이미 한번 가본곳도 가지 않는다.
            if visited[next_row][next_col] != 0:
                continue
            #간곳이니 체크하고, 재귀함수 들어간다. 그곳이 아니면 값을 돌아와야하니깐 값을 다시 풀어준다.
            visited[next_row][next_col] = 1
            cnt += 1
            dfs(next_row, next_col, path.append(MAP[row][col]))
            visited[next_row][next_col] = 0

    return ans

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    ans = 0
    cnt = 1

    #그래프 구성
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    #시작값 찾기
    start_row = 0
    start_col = 0
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 2:
                start_row = row
                start_col = col

    ans2 = dfs(start_row, start_col)
    print(f"#{tc} {ans} {ans2}")



    




