'''

도로가 파여진 깊이에 비례해서 복구 시간은 증가한다.

거리는 고려 x => 즉 몇칸을 이동하는지!

=> 출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하라!


깊이가 1이라면 복구에 드는 시간이 1이라고 가정한다.



풀이가 3가지 나온다!

1) 다익스트라 => 가중치가 다르다고 보면 되는구나 이것도! 가는 칸마다!

2) bfs

3) dfs

세가지 다 풀어보자 구나!!



'''

# import heapq
#
# INF = int(1e9)
#
# T = int(input())
#
#
# for tc in range(1, T + 1):
#
#
#     #1. 그래프 구성
#     N = int(input())
#
#     MAP = [list(map(int, input())) for _ in range(N)]
#
#     distance = [[INF] * N for _ in range(N)]
#
#     #2. 힙큐 생성
#
#     hq = []
#
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     #3.초기값 설정! => 시작점 아,, 이차원 배열이라 코스트가 필요하지는 않겠구나! 간선의 길이값!
#
#     heapq.heappush(hq, (0,0))
#     distance[0][0] = 0
#
#     while hq:
#
#     #4. 가장 최소의 값 꺼내기
#         now = heapq.heappop(hq)
#         now_row = now[0]
#         now_col = now[1]
#
#
#     #5. next값을 찾기
#
#         for dir in range(4):
#             next_row = now_row + dr[dir]
#             next_col = now_col + dc[dir]
#
#             #범위 체크
#             if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
#                 continue
#
#             if distance[now_row][now_col] + MAP[next_row][next_col] >= distance[next_row][next_col]:
#                 continue
#             distance[next_row][next_col] = distance[now_row][now_col] + MAP[next_row][next_col]
#             heapq.heappush(hq,(next_row, next_col))
#
#     print(f"#{tc} {distance[N-1][N-1]}")




def dfs(row, col, cnt):

    global ans

    if row == N - 1 and col == N - 1:
        ans = min(ans, cnt)
        return

    if ans <= cnt:
        return

    for dir in range(4):
        next_row = row + dr[dir]
        next_col = col + dc[dir]

        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
            continue

        if visited[next_row][next_col] != 0: #한반 간곳은 가지 않아!
            continue

        visited[next_row][next_col] = 1

        dfs(next_row, next_col, cnt + int(MAP[next_row][next_col]))

        visited[next_row][next_col] = 0


#DFS로 풀어보자!


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T + 1):


    N = int(input())
    MAP = [list(input().rstrip()) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    visited[0][0] = 1

    ans = 987654321

    dfs(0,0,0)

    print(f"#{tc} {ans}")
